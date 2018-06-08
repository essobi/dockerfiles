FROM ubuntu:12.04  
  
# Update package repository  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe
multiverse" > /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y wget make curl software-properties-common  
ADD . /root/rackspace-uploader  
RUN cd /root/rackspace-uploader && make install  
ENTRYPOINT ["/usr/local/bin/rackspace-uploader"]

