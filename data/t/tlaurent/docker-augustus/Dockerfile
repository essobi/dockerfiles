FROM phusion/baseimage  
  
MAINTAINER Timothy Laurent timothyjlaurent@gmail.com  
  
RUN apt-get update;\  
apt-get install -y -q libboost-iostreams-dev libboost-system-dev libboost-
filesystem-dev zlibc wget build-essential;\  
apt-get upgrade -y -q;\  
mkdir /build;\  
cd /build;\  
wget http://bioinf.uni-
greifswald.de/augustus/binaries/augustus.current.tar.gz;\  
tar -xaf augustus*;\  
rm *.gz;\  
cd `ls -d -1 augustus*`;\  
cd src;\  
make && cd .. && make install;\  
cd / && rm -rf /build;\  
apt-get purge -y build-essential;\  
apt-get clean  
  
## this puts all the bins in /opt/augustus3.0.2 and links it to a path
location  
## Now we will create root level /data directory and /config as a locatioon to
mount input  
## data and easily access config settings  
RUN mkdir /config ; mkdir /data;\  
echo "/config" > /etc/container_environment/AUGUSTUS_CONFIG_PATH  
  
VOLUME ["/config","/data"]  
  
ENTRYPOINT ["/sbin/my_init","--"]  

