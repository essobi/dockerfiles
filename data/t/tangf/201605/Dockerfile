FROM debian:jessie  
  
MAINTAINER tangf <316907331@qq.com>  
  
RUN apt-get update; \  
apt-get -y install g++ git subversion  
  
RUN mkdir /var/www/html; \  
cd /var/www/html; \  
git clone https://github.com/tang-f/201605.git ; \  
cd 201605; \  
rm -rf apache .git README.md;  
  
WORKDIR /var/www/html  
  

