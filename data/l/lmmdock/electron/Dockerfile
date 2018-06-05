FROM node:latest  
  
MAINTAINER Leonard Marschke <leonard@marschke.me>  
  
RUN apt-get update && \  
apt-get install -y libgtk2.0-0 libgconf-2-4 \  
libasound2 libxtst6 libxss1 libnss3 xvfb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

