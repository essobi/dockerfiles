FROM ubuntu:trusty  
MAINTAINER Takashi Kawachi <tkawachi@gmail.com>  
  
# Install utility commands  
RUN sudo apt-get update  
RUN sudo apt-get install -y ruby python python-pip  
RUN sudo pip install awscli  
  
ADD ./cloudwatch-alert.rb /usr/local/bin/cloudwatch-alert.rb  
RUN chmod 0755 /usr/local/bin/cloudwatch-alert.rb  
ENTRYPOINT /usr/local/bin/cloudwatch-alert.rb  

