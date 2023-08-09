# Directory Search Tool

A simple Python script for performing directory searches on a URL using a wordlist.

## Description

This script allows you to perform directory searches on a given URL using a provided wordlist. It uses multithreading to speed up the search process.

## Usage

1. Install the required Python packages:
   
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:

   ```bash
   python dirsearch.py -w path/to/wordlist.txt -u http://example.com
   ```

   Replace `path/to/wordlist.txt` with the actual path to your wordlist file and `http://example.com` with the URL you want to perform the directory search on.

## Running with Docker
Build the Docker image:

```bash
docker build -t dirsearch .
```

Run the Docker container with a mounted volume for the wordlist:

```bash
docker run -it --rm -v /path/to/wordlist:/app/wordlist.txt dirsearch -w /app/wordlist.txt -u http://example.com
```

Replace /path/to/wordlist with the actual path to your wordlist file on your host system and http://example.com with the URL you want to perform the directory search on.

## Options

- `-w`, `--wordlist`: Path to the wordlist file (required).
- `-u`, `--url`: URL to perform the directory search on (required).
- `--status-filter`: Filter URLs by specific status codes (optional).
- `--max-threads`: Sets the maximum number of threads (default 40) (optional).
- `--min-response-length`: Minimum length of response content (optional).
- `--max-response-length`: Maximum length of response content (optional).

## Example

Perform a directory search on http://example.com with status code filter 200 and 403, minimum word length 4, and minimum response length 100:

```bash
python dirsearch.py -w path/to/wordlist.txt -u http://example.com --status-filter 200 403 --min-word-length 4 --min-response-length 100
```

## Requirements

- Python 3.8
- See `requirements.txt` for external package dependencies.