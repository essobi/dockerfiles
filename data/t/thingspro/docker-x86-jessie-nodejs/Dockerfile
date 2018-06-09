FROM node:8.11.2  
  
LABEL author="Zack Yang <zack9433@gmail.com>"  
  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
debhelper \  
devscripts \  
dh-make \  
dh-systemd \  
git-buildpackage \  
fakeroot && rm -rf /var/lib/apt/lists/*  
  
WORKDIR /app  

