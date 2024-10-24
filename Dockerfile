# Use an official Anaconda base image
FROM python:3.9

# Set working directory in the container
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the current project code into the working directory
COPY . .

# Optionally expose a port (if your project is a web app or needs to serve something)
# EXPOSE 8000

# Command to run your application (adjust according to your entry point script)
CMD ["python", "main.py"]
# ENTRYPOINT ["tail"]
# CMD ["-f","/dev/null"]