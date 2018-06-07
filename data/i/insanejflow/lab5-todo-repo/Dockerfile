############################################################  
# Dockerfile to build Python WSGI Application Containers  
# Based on Ubuntu  
############################################################  
# Set the base image to Ubuntu  
FROM ubuntu:latest  
# File Author / Maintainer  
MAINTAINER JooeunAhn  
  
# Update the sources list  
RUN apt-get update  
# Install Python and Basic Python Tools  
RUN apt-get install -y python3 python3-pip mysql-client libmysqlclient-dev  
#copy app.py into /app folder  
ADD /lab5 /lab5  
  
# Copy the application folder inside the container  
#COPY /templates /app/  
# Upgrade PIP  
RUN pip3 install --upgrade pip  
# Get pip to download and install requirements:  
RUN pip3 install -r /lab5/requirements.txt  
# Expose ports  
EXPOSE 8000  
# Set the default directory where CMD will execute  
WORKDIR /lab5  
# Set the default command to execute  
# when creating a new container  
CMD python3 manage.py runserver 0.0.0.0:8000  

