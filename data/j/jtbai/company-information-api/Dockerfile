# Use an official Python runtime as a base image  
FROM python:3.4-slim  
  
# Set the working directory to /app  
WORKDIR /  
  
# Copy the current directory contents into the container at /app  
ADD . /  
  
# Installing all gcc dependancies  
RUN apt-get update  
RUN apt-get install -y gcc python3-all-dev  
RUN apt-get install -y python3-openssl  
RUN apt-get install -y build-essential libssl-dev libffi-dev  
  
# Install any needed packages specified in requirements.txt  
RUN pip install -r requirements.txt  
  
# Make port 5000 available to the world outside this container  
EXPOSE 5000  
# Run app.py when the container launches  
CMD ["python","api.py"]  

