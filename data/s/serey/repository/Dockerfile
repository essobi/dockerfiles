# Use an official Python runtime as a base image  
FROM python:2.7-slim  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
ADD . /app  
  
# Install any needed packages specified in requirements.txt  
RUN pip install -r requirements.txt  
  
# Make port 80 available to the world outside this container  
EXPOSE 80  
# Define environment variable  
ENV NAME username_id  
  
# Run app.py when the container launches  
CMD ["python", "app.py"]  
  
#CMD  
# Used for executing commands when we build  
# a new container from the docker image.

