FROM libreelec/python:1.0.1  
MAINTAINER docker@libreelec.tv  
  
RUN wget -O -
https://github.com/SickGear/SickGear/archive/release_0.11.11.tar.gz | tar xzf
- \  
&& mv /SickGear-release_0.11.11 /sickgear  
  
EXPOSE 8081  
VOLUME ["/config", "/data"]  
  
CMD ["/usr/bin/python", "/sickgear/SickBeard.py", "--datadir", "/data", "--
config","/config/config.ini", "--nolaunch"]  

