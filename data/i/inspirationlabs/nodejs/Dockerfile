# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.16  
MAINTAINER Dominic Böttger  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo bash -  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y nodejs ssh git build-essential python pkg-config  
RUN apt-get install -y catdoc poppler-utils tesseract-ocr unzip  
RUN mkdir /var/node  
  
# Clean up  
WORKDIR /  
RUN apt-get autoremove -y && \  
apt-get autoclean && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install -g bower  
  
ADD ssh_config /etc/ssh/ssh_config  
  
ADD run.sh /  
RUN chmod +x /run.sh  
  
WORKDIR /var/node  
VOLUME ["/var/node"]  
EXPOSE 3000  
EXPOSE 3443  
CMD ["/run.sh"]  

