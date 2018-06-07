# Use an official Python runtime as a parent image  
FROM python:2.7-slim  
  
# Copy the current directory contents into the container at /  
ADD . /  
  
# Install any needed packages specified in requirements.txt  
# RUN pip install -r requirements.txt  
# Make port 11111 available to the world outside this container  
EXPOSE 11111  
# Define environment variable  
# ENV NAME World  
# Run server.py when the container launches  
CMD ["python", "server.py"]

