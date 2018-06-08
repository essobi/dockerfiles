FROM ubuntu-debootstrap:vivid  
  
RUN \  
set -eux ;\  
echo "deb http://archive.ubuntu.com/ubuntu vivid multiverse" >
/etc/apt/sources.list.d/multiverse.list ;\  
echo "deb http://ppa.launchpad.net/libretro/stable/ubuntu vivid main" >
/etc/apt/sources.list.d/libretro.list ;\  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 18DAAE7FECA3745F ;\  
apt-get update ;\  
apt-get install -y libretro-* retroarch ;\  
apt-get clean  
  
WORKDIR /root  
ENTRYPOINT retroarch  

