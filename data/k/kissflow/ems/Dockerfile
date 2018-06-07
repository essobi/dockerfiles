FROM ubuntu:latest  
  
MAINTAINER Vivek Madurai "vivek.madurai@orangescape.com"  
RUN apt-get clean  
RUN apt-get update -y  
RUN apt-get install -y python3-pip python3-dev build-essential  
RUN pip3 install --upgrade pip  
  
COPY . /app  
WORKDIR /app  
  
RUN pip3 install -r requirements.txt  
  
# Environment Variables  
ENV ENV prd

