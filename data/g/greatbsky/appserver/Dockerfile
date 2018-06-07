FROM greatbsky/tomcat:latest  
MAINTAINER architect.bian  
LABEL name="appserver" license="MIT" build-date="20170223"  
  
ENV VERSION 1.0.0  
ENV GM_VERSION 1.3.25  
RUN yum update -y && yum install -y libjpeg libjpeg-devel libpng libpng-devel
giflib giflib-devel freetype freetype-devel && cd /data/softs && wget -O
GraphicsMagick.tar.gz
https://sourceforge.net/projects/graphicsmagick/files/graphicsmagick/$GM_VERSION/GraphicsMagick-$GM_VERSION.tar.gz/download
&& tar -zxf GraphicsMagick.tar.gz && cd GraphicsMagick-$GM_VERSION &&
./configure && make && make install && rm -rf /data/softs/*  
  
CMD ["/data/env/tomcats/0/bin/catalina.sh", "run"]  

