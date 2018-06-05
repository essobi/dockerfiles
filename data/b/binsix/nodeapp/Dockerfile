FROM binsix/node.js:latest  
MAINTAINER LiuBin  
LABEL name="nodeapp" license="MIT" build-date="20170812"  
  
ENV NODE_VERSION v8.2.1  
RUN yum update -y && mkdir -p /data/softs/graphicsmagick && cd
/data/softs/graphicsmagick && wget
https://sourceforge.net/projects/graphicsmagick/files/graphicsmagick/1.3.25/GraphicsMagick-1.3.25.tar.gz
&& tar -xvf GraphicsMagick-1.3.25.tar.gz && cd GraphicsMagick-1.3.25 &&
./configure && make && make install && yum install -y cairo cairo-devel
cairomm-devel libjpeg-turbo-devel pango pango-devel pangomm pangomm-devel
giflib-devel && npm install canvas  
  
CMD ["node", "-v"]  

