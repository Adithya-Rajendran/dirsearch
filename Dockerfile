# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make main.py executable
RUN chmod +x dirsearch.py

# Run the command when the container launches
CMD ["./dirsearch.py"]