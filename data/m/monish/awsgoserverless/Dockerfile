FROM golang:1.9.1  
LABEL version="0.4"  
LABEL description="This image provides tools to build & deploy Go applications
to AWS using serverless framework"  
MAINTAINER hello@moni.sh  
  
# Install deps  
RUN apt-get update  
RUN apt-get install -y python python-pip groff less curl  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g serverless  
RUN pip install awscli  

