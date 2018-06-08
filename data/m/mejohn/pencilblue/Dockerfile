FROM fedora:latest  
MAINTAINER Meaghan Johnson <mejohn10@ncsu.edu>  
  
# yum installs  
RUN yum -y update && yum -y install \  
curl \  
git \  
mongodb \  
mongodb-server \  
nodejs \  
npm  
  
# npm installs  
RUN npm install -g \  
nodemon \  
pencilblue-cli  
  
# MongoDB configuration  
RUN mkdir -p /var/lib/mongodb && \  
touch /var/lib/mongodb/.keep && \  
chown -R mongodb:mongodb /var/lib/mongodb  
ADD mongodb.conf /etc/mongodb.conf  
  
# PencilBlue installation  
RUN mkdir -p /root/pb \  
&& cd /root/pb \  
&& git clone https://github.com/pencilblue/pencilblue.git /root/pb \  
&& npm install  
ADD config.js /root/pb/config.js  
  
WORKDIR /root/pb  
ENTRYPOINT /usr/bin/mongod --config /etc/mongodb.conf && pencilblue start  
EXPOSE 27017 49500  

