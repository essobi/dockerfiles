# this is the base image for all world images  
FROM debian:jessie  
  
MAINTAINER "Mogria <m0gr14@gmail.com>"  
RUN apt-get update && \  
apt-get install -y wget && \  
wget "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-
linux$(getconf LONG_BIT)" -O /usr/bin/jq && \  
chmod +x /usr/bin/jq && \  
apt-get purge -y wget  
  
ADD create-player.sh /home/create-player.sh  
ADD genfunc.sh /usr/bin/genfunc.sh  
ADD gen.sh /usr/bin/gen  
  
RUN groupadd \--gid 1312 rtshplayers && \  
useradd \--uid 1337 rtshsrv && \  
chmod +x /home/create-player.sh && \  
mkdir /world && \  
chown -R rtshsrv:rtshsrv /world && \  
chmod +x /usr/bin/gen  
  
VOLUME ["/home"]  
  
ENTRYPOINT ["/bin/true"]  

