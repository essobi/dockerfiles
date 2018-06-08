#Use an official Python runtime as a base image  
FROM python:3.6  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
ADD . /app  
  
# Install any needed packages specified in requirements.txt  
RUN pip install -r requirements.txt  
  
# Make port 80 available to the world outside this container  
EXPOSE 80  
# Run start the gunicorn webserver when the container launches  
CMD ["gunicorn", "--config=gunicorn.py", "main:app"]  

