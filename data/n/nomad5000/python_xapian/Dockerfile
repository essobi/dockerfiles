############################################################  
# Dockerfile to run a Django-based web application  
# Based on an Ubuntu Image  
############################################################  
# Set the base image to use to Ubuntu  
FROM python:2  
# Set the file maintainer (your name - the file's author)  
MAINTAINER Michael Schmidt  
  
RUN apt-get update && apt-get -y install uuid-dev python-xapian  
  
WORKDIR ~  
RUN curl -O http://oligarchy.co.uk/xapian/1.2.21/xapian-core-1.2.21.tar.xz \  
&& tar -xvf xapian-core-1.2.21.tar.xz \  
&& cd xapian-core-1.2.21 && ./configure && make && make install  
RUN curl -O http://oligarchy.co.uk/xapian/1.2.21/xapian-bindings-1.2.21.tar.xz
\  
&& tar -xvf xapian-bindings-1.2.21.tar.xz \  
&& cd xapian-bindings-1.2.21 && ./configure --with-python && make && make
install  
RUN rm -rf xapian-*  
  

