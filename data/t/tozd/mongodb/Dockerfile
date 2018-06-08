FROM tozd/runit:ubuntu-xenial  
  
EXPOSE 27017/tcp  
  
VOLUME /var/lib/mongodb  
VOLUME /var/log/mongod  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6 && \  
echo "deb http://repo.mongodb.org/apt/ubuntu $(cat /etc/lsb-release | grep
DISTRIB_CODENAME | cut -d= -f2)/mongodb-org/3.4 multiverse" >
/etc/apt/sources.list.d/mongodb.list && \  
apt-get update -q -q && \  
apt-get install --yes --force-yes mongodb-org  
  
COPY ./etc /etc  

