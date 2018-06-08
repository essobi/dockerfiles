FROM libreelec/python:1.0.1  
MAINTAINER docker@libreelec.tv  
  
RUN wget -O -
https://github.com/CouchPotato/CouchPotatoServer/archive/build/3.0.1.tar.gz |
tar xzf - \  
&& mv /CouchPotatoServer-build-3.0.1 /CouchPotatoServer  
  
EXPOSE 5050  
VOLUME ["/config", "/data"]  
  
CMD ["/usr/bin/python", "/CouchPotatoServer/CouchPotato.py", "--data_dir",
"/data", "--config_file","/config/CouchPotato.cfg", "--console_log"]  

