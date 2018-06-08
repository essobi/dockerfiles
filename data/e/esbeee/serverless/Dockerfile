FROM node:9.6.1  
  
# Installing python and pip as the latter is the documented way to install the  
# AWS CLI.  
# Install python.  
RUN apt-get update -qq && \  
apt-get install -y python-dev && \  
apt-get clean  
  
# Install pip.  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
# Install AWS CLI and dependecies.  
RUN pip install awscli  
RUN apt-get update -qq && \  
apt-get install -y groff && \  
apt-get clean  
  
# Install serverless.  
RUN npm install -g serverless@1.26.1  

