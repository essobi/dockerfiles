# Use an official Python 2.7 runtime  
FROM python:2.7-slim  
  
# Set workdirectory  
WORKDIR /app  
  
# Copy current directory contents into the container /app  
ADD . /app  
  
# Install any needed packages specified in requirements.txt  
RUN pip install -r requirments.txt  
  
# Make port 80 available outside the docker  
EXPOSE 80  
# Define environment variable  
ENV NAME World  
  
# Run app.py  
CMD ["python", "app.py"]  

