import argparse
import requests
import concurrent.futures

def load_wordlist(wordlist_path):
    with open(wordlist_path, 'r', encoding='iso-8859-1') as file:
        wordlist = [line.strip() for line in file]
    return wordlist


def search_directory(url, word, status_filter=None, min_response_length=None, max_response_length=None):
    full_url = f"{url}/{word}"
    response = requests.get(full_url)

    # Skip the print statement if the filter fails
    if status_filter and response.status_code not in status_filter:
        return
    if min_response_length and len(response.text) < min_response_length:
        return
    if max_response_length and len(response.text) > max_response_length:
        return

    print(f"Found: {full_url} (Status: {response.status_code}, Response Length: {len(response.text)})")


def main():
    parser = argparse.ArgumentParser(description="Simple directory search using a wordlist")
    parser.add_argument("-w", "--wordlist", help="Path to the wordlist file", required=True)
    parser.add_argument("-u", "--url", help="URL to perform directory search on", required=True)
    parser.add_argument("--status-filter", type=int, nargs="+", help="Filter URLs by specific status codes (multiple codes seperated by spaces)")
    parser.add_argument("--max-threads", type=int, default=40, help="Maximum number of threads")
    parser.add_argument("--min-response-length", type=int, help="Minimum length of response content")
    parser.add_argument("--max-response-length", type=int, help="Maximum length of response content")
    args = parser.parse_args()

    print(args.wordlist)
    wordlist = load_wordlist(args.wordlist)

    # Multithreaded to add concurrency
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_threads) as executor:
        # Using the map function to link each word to the filters
        executor.map(search_directory, 
                     [args.url] * len(wordlist), 
                     wordlist, 
                     [args.status_filter] * len(wordlist), 
                     [args.min_response_length] * len(wordlist),
                     [args.max_response_length] * len(wordlist))

    return


if __name__ == "__main__":
    main()