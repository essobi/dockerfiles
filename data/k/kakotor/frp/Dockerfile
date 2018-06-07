# This dockerfile uses the ubuntu image  
# VERSION 1 - EDITION 1  
# Author: kakotor  
# Command format: Instruction [arguments / command] ..  
# Base image to use, this must be set as the first line  
FROM ubuntu:latest  
  
RUN mkdir -p /opt/frp  
  
COPY frps /opt/frp/frps  
RUN chmod +x /opt/frp/frps  
COPY frps.ini /opt/frp/frps.ini  
  
EXPOSE 4443 4444 80  
ENTRYPOINT /opt/frp/frps -c /opt/frp/frps.ini  

