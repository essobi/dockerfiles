# Using official python runtime base image  
FROM python:2.7  
# Install our requirements.txt  
RUN mkdir /code  
WORKDIR /code  
ADD requirements.txt /code/  
RUN pip install -r requirements.txt  
ADD . /code/  
  
# Make port 5000 available for links and/or publish  
EXPOSE 80

