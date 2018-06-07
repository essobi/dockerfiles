# installing jq  
#  
# VERSION 0.1  
# Pull base image.  
FROM debian  
  
# :)  
MAINTAINER Tazro Inutano Ohta, inutano@gmail.com  
  
# Install packages.  
RUN apt-get update && \  
apt-get install -y wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Install xml-to-json  
WORKDIR /bin  
RUN wget "http://stedolan.github.io/jq/download/linux64/jq" && chmod 755 jq  
  
# Define working directory.  
WORKDIR /data  
  
# Default command  
CMD ["/bin/jq"]  

