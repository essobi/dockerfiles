FROM ubuntu:16.04  
  
MAINTAINER Alexey Nurgaliev <atnurgaliev@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
ADD setup.sh /usr/local/firebird_setup.sh  
  
RUN apt-get update &&\  
apt-get upgrade -y &&\  
apt-get install -y libncurses5-dev bzip2 curl gcc g++ make &&\  
  
mkdir -p /tmp/firebird &&\  
cd /tmp/firebird &&\  
curl -L -o firebird.tar.bz2 \  
"http://sourceforge.net/projects/firebird/files/firebird/2.5.6-Release/Firebird-2.5.6.27020-0.tar.bz2"
&&\  
tar \--strip=1 -xf firebird.tar.bz2 &&\  
  
./configure --enable-superserver \--prefix=/usr/local/firebird &&\  
make &&\  
make silent_install &&\  
  
cd / &&\  
rm -R /tmp/firebird &&\  
  
bash /usr/local/firebird_setup.sh &&\  
rm /usr/local/firebird_setup.sh &&\  
  
apt-get purge -y --auto-remove libncurses5-dev bzip2 curl gcc g++ make  
  
VOLUME ["/sqlbase"]  
  
EXPOSE 3050  
  
ENTRYPOINT ["/usr/local/firebird/bin/fbguard"]  

