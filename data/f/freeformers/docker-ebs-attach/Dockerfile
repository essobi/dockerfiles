FROM ubuntu:14.04  
MAINTAINER Shaun Stanworth "shaun@freeformers.com"  
#  
# install deps/tools  
#  
RUN apt-get -q update  
RUN apt-get install -y python-requests python-boto  
  
ADD ebs-attach.py ebs-attach.py  
  
ENTRYPOINT ["/usr/bin/python", "ebs-attach.py"]  

