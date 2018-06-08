FROM ubuntu:16.04  
LABEL maintainer="Marco Antonio Martins Junior <somatorio@gmail.com>"  
  
RUN \  
echo "deb http://archive.ubuntu.com/ubuntu xenial multiverse" >
/etc/apt/sources.list.d/multiverse.list && \  
echo "deb http://ppa.launchpad.net/libretro/stable/ubuntu xenial main" >
/etc/apt/sources.list.d/libretro.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 18DAAE7FECA3745F && \  
apt-get update && \  
apt-get install -y libretro-* retroarch --no-install-recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root  
ENTRYPOINT [ "/usr/bin/retroarch" ]  

