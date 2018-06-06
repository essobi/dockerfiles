FROM garo/easy-xpra:latest  
MAINTAINER Nikolas Garofil "nikolas@garofil.be"  
  
#Install spotify, everything is on 1 layer to shrink image size (e.g. cleaning
the apt cache on a new layer is pretty useless because the layer before still
contains this data)  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install gpg &&
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
0DF731E45CE24F27EEEB1450EFDC8610341D9410 && echo deb
http://repository.spotify.com stable non-free | tee
/etc/apt/sources.list.d/spotify.list && apt-get update &&
DEBIAN_FRONTEND=noninteractive apt-get -y install spotify-client && apt-get -y
purge gpg && apt-get -y \--purge autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Run spotify in xpra  
CMD ["run_in_xpra", "spotify"]  

