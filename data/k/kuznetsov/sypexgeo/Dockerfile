FROM node:6.7.0-onbuild  
  
RUN \  
apt-get update &&\  
apt-get -y install unzip &&\  
wget http://sypexgeo.net/files/SxGeoCity_utf8.zip &&\  
unzip SxGeoCity_utf8.zip &&\  
rm SxGeoCity_utf8.zip &&\  
apt-get -y remove unzip &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3000  

