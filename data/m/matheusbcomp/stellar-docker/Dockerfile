# Use an official Python runtime as a parent image  
FROM python:3.5  
# Set the working directory to /code  
WORKDIR /code  
  
# Create the django user and take ownership of /code  
RUN adduser --no-create-home --disabled-login --group --system django && \  
chown -R django:django /code  
  
# Copy the pip requirementes file to /code  
COPY requirements.txt /code  
  
# Install any needed packages specified in requirements.txt  
RUN pip install -r requirements.txt  
  
# Execute start script  
CMD ["/bin/bash", "-c", "python"]  
  

