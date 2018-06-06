FROM ubuntu:16.04  
LABEL maintainer="Daniel.Castellani@nyu.edu"  
  
ENV PYTHONUNBUFFERED 1  
  
COPY apt-get.txt /tmp/  
  
RUN apt-get update -y && apt-get install -y $(grep -vE "^\s*#" /tmp/apt-
get.txt | tr "\n" " ")  
RUN echo "America/New_York" | tee /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
RUN apt-get upgrade -y  
  
  
  
  
  

