# Use an official Anaconda base image
FROM python:3.9

# Set working directory in the container
WORKDIR /app

# Install FFmpeg and other necessary packages
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the current project code into the working directory
COPY . .

# Optionally expose a port (if your project is a web app or needs to serve something)
# EXPOSE 8080

# Command to run your application (adjust according to your entry point script)
WORKDIR /app/project
CMD ["python", "main.py"]
# ENTRYPOINT ["tail"]
# CMD ["-f","/dev/null"]