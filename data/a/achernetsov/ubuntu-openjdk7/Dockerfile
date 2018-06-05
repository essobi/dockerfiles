# https://askubuntu.com/a/803616/198724  
FROM phusion/baseimage:latest  
  
RUN apt-get update && apt-get install -y debian-archive-keyring software-
properties-common  
RUN add-apt-repository 'deb http://httpredir.debian.org/debian experimental
main'  
RUN add-apt-repository 'deb http://httpredir.debian.org/debian sid main'  
  
COPY debian /etc/apt/preferences.d/debian  
  
RUN apt-get update && apt-get install -y openjdk-7-jdk

