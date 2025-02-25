# Use the official Python image from the Docker Hub
FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY . /app

# Install the dependencies
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate 

# Copy the rest of the application code into the container
#COPY . .

# Specify the command to run the application
CMD ["python3", "app.py"]