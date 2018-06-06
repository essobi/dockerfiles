# https://docs.docker.com/get-started/part2/#define-a-container-with-a-
dockerfile  
# Use an official Python runtime as a parent image  
FROM python:3-alpine  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
ADD . /app  
  
# Install any needed packages specified in requirements.txt  
RUN pip install -r requirements.txt  
  
# Run app.py when the container launches  
CMD ["./server.py", "--mpd-hostname=mpd.chaosdorf.space", "--mqtt-
hostname=mqttserver.chaosdorf.space"]  

