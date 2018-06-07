# Base image  
FROM maven:3.5.2-jdk-8  
# Set the working directory  
WORKDIR /tmp  
  
# Copy the contents of the transfer directory to the image  
COPY transfer /tmp  
  
# Install required software  
RUN apt update  
RUN apt install -y python-pip  
RUN pip install --trusted-host pypi.python.org -r requirements.txt  

