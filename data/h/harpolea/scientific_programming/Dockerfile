# Use an official Python runtime as a base image  
FROM python:3.5-slim  
  
# Set the working directory to /src  
WORKDIR /src  
  
# Copy the current directory contents into the container at /src  
ADD . /src  
  
# Install any needed packages specified in requirements.txt  
RUN pip install -r requirements.txt  
  
# Run app.py when the container launches  
CMD ["python", "example_app.py"]  

