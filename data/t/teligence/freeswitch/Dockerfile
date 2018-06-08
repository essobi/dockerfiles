FROM debian:jessie  
  
RUN apt-get -y update && apt-get install -y curl && \  
echo "deb http://files.freeswitch.org/repo/deb/debian/ jessie main" >
/etc/apt/sources.list.d/freeswitch.list && \  
echo "deb http://files.freeswitch.org/repo/deb/freeswitch-1.6/ jessie main" >
/etc/apt/sources.list.d/99FreeSWITCH.test.list && \  
curl -s http://files.freeswitch.org/repo/deb/freeswitch-1.6/key.gpg | apt-key
add \- && \  
apt-get -y update && apt-get install -y \  
libyuv \  
freeswitch-meta-vanilla && \  
  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
CMD ["freeswitch", "-nonat"]  

