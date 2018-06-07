# Dockerfile can be used in custom box installation if needed.  
FROM ubuntu:14.04  
MAINTAINER Yixin Xia "yixin@iflyworld.«com"  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Update packages  
RUN apt-get update -y && apt-get upgrade -y  
  
# Install some packages we need  
RUN apt-get install -y build-essential git curl python  
  
# Install latest version of pip  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py  
  
# Install Node.JS  
RUN cd /usr/local && curl
http://nodejs.org/dist/v6.11.0/node-v6.11.0-linux-x64.tar.gz | tar --strip-
components=1 -zxf-  
  
# Install AWS CLI  
RUN pip install awscli awsebcli  
  
# Install Ruby and SASS  
RUN apt-get update -y && \  
apt-get install -y ruby  
RUN gem install sass  
  
# Make sure we land in a shell  
CMD ["/bin/bash"]

