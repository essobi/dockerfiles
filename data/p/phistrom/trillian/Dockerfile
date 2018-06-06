FROM ubuntu:14.04  
MAINTAINER Phillip Stromberg <phillip@stromberg.me>  
LABEL Description="Trillian is a chat client from Cerulean Studios that
supports multiple protocols. This is their Linux client which is in beta."  
  
RUN apt-get update && apt-get install -y \  
dbus-x11 \  
wget  
RUN wget -qP /etc/apt/sources.list.d/
https://www.trillian.im/get/linux/2.0/apt/trillian.list && \  
wget -qO - https://www.trillian.im/get/linux/2.0/apt/trillian.key | apt-key
add - && \  
apt-get update && \  
apt-get install -y trillian  
  
RUN useradd -m -d /trillian trillian  
RUN mkdir /trillian/.trillian && \  
chown trillian:trillian /trillian/.trillian  
WORKDIR /trillian  
USER trillian  
  
ENTRYPOINT /usr/bin/trillian  
  

