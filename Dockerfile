# Use an official Anaconda base image
FROM continuumio/anaconda3:latest

# Set working directory in the container
WORKDIR /app

# Copy the environment YAML file (if you use conda for environment management)
COPY environment.yml .

# Install dependencies from the environment.yml
RUN conda env create -f environment.yml

# Activate the environment
SHELL ["conda", "run", "-n", "discord-bot-env", "/bin/bash", "-c"]

# Copy the current project code into the working directory
COPY . .

# Optionally expose a port (if your project is a web app or needs to serve something)
# EXPOSE 8000

# Command to run your application (adjust according to your entry point script)
CMD ["python", "main.py"]
