FROM ubuntu:14.04  
MAINTAINER Alex Bernard <alexis.bernard33@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y mumble-server  
  
EXPOSE 64738 64738/udp  
  
WORKDIR /mumble  
  
COPY mumble-server.ini /mumble/  
COPY start.py /mumble/  
  
CMD ["/usr/bin/python3", "start.py"]

