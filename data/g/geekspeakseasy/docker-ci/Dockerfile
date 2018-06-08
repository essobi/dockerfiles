#Download base image ubuntu 16.04  
FROM ubuntu:16.04  
# Update Ubuntu Software repository  
RUN apt-get update  
  
# Install Node...  
RUN apt-get install -y nodejs  
  
RUN apt-get install -y npm  
  
# Copy app to /src  
COPY . /src  
  
# Install app and dependencies into /src  
RUN cd /src; npm install  
  
EXPOSE 8080  
CMD cd /src && node ./app.js  
  
# This base image works. Keep this configuration.  
# Next autodeploy from Docker to AWS EC2.

