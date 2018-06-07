FROM ubuntu:xenial  
  
RUN apt-get -y update && apt-get install -y wget && \  
echo "deb http://rpms.litespeedtech.com/debian/ xenial main" >
/etc/apt/sources.list.d/openlitespeed.list && \  
wget -O- http://rpms.litespeedtech.com/debian/lst_repo.gpg | apt-key add && \  
apt-get -y update && apt-get install -y openlitespeed  
  
  

