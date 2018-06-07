FROM ubuntu:trusty  
  
MAINTAINER mnagaku <mnagaku@gmail.com>  
  
RUN echo "Asia/Tokyo" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata && locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
ENV LC_ALL en_US.UTF-8  
  
RUN sed -i".bak" -e 's/\/\/archive.ubuntu.com/\/\/ftp.jaist.ac.jp/g'
/etc/apt/sources.list &&\  
apt-get update && apt-get upgrade -y &&\  
apt-get -y install wget unzip build-essential curl python libpq-dev &&\  
wget -qO- https://deb.nodesource.com/setup_0.12 | bash - &&\  
apt-get update && apt-get upgrade -y && apt-get -y install nodejs &&\  
wget https://github.com/ether/etherpad-lite/archive/master.zip &&\  
unzip master && rm -f master.zip &&\  
etherpad-lite-master/bin/installDeps.sh &&\  
npm install sqlite3 ep_headings ep_monospace_default ep_print &&\  
sed 's/"requireAuthentication": false,/"requireAuthentication": true,/g'
etherpad-lite-master/settings.json -i &&\  
sed 's/"dbType" : "dirty",/"dbType" : "sqlite",/g' etherpad-lite-
master/settings.json -i &&\  
sed 's/"filename" : "var\/dirty.db"/"filename" : "var\/ep.sq3"/g' etherpad-
lite-master/settings.json -i &&\  
sed 's/available! \\*\//available!
\\*\/\n"users":{"admin":{"password":"changeme1","is_admin":true},"user":{"password":"changeme1","is_admin":false}},/g'
etherpad-lite-master/settings.json -i &&\  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
EXPOSE 9001  
  
CMD etherpad-lite-master/bin/run.sh \--root  

