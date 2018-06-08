FROM debian:8  
MAINTAINER Mike Clarke <michaelclarkecs@gmail.com>  
  
RUN echo "deb http://overviewer.org/debian ./" >
/etc/apt/sources.list.d/overviewer.list \  
&& apt-get update \  
&& apt-get install -y wget \  
&& wget -O - http://overviewer.org/debian/overviewer.gpg.asc | apt-key add - \  
&& apt-get update \  
&& apt-get install -y minecraft-overviewer  
RUN useradd -ms /bin/bash overviewer  
RUN wget -O /texturepack https://dl.dropboxusercontent.com/u/75066972/Tiny\
Pixels\ -\ 25th\ October.zip  
COPY overviewer.config /  
  
VOLUME ["/world"]  
VOLUME ["/map"]  
USER overviewer  
  
ENTRYPOINT ["overviewer.py", "--config=/overviewer.config"]  

