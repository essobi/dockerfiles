FROM vladus2000/ubuntu-base  
MAINTAINER vladus2000 <docker@matt.land>  
  
COPY shiz/ /  
  
RUN \  
apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install gnupg && \  
echo deb http://APT.spideroak.com/ubuntu-spideroak-hardy/ release restricted >
/etc/apt/sources.list.d/spideroakone.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 573E3D1C51AE1B3D && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::=--force-confnew
install spideroakone && \  
apt-get -y purge gnupg && \  
apt-get -y autoremove && \  
apt-get clean && \  
chmod +x /startup.sh  
  
CMD /bin/bash -c /startup.sh  
  
VOLUME /root/.config/SpiderOakONE/  
VOLUME /home/user/.config/SpiderOakONE/  
VOLUME /root/SpiderOak Hive/  
VOLUME /home/user/SpiderOak Hive/  
  

