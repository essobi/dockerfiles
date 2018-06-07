FROM greatbsky/node.js:latest  
MAINTAINER architect.bian LiuBin  
LABEL name="nodeapp" license="MIT" build-date="20170808"  
  
ENV VERSION 8.2.1  
ENV GRAPHICSMAGICK_VERSION 1.3.25  
RUN yum update -y && mkdir -p /data/softs/graphicsmagick && cd
/data/softs/graphicsmagick && wget
https://sourceforge.net/projects/graphicsmagick/files/graphicsmagick/$GRAPHICSMAGICK_VERSION/GraphicsMagick-$GRAPHICSMAGICK_VERSION.tar.gz
&& tar -xvf GraphicsMagick-$GRAPHICSMAGICK_VERSION.tar.gz && cd
GraphicsMagick-$GRAPHICSMAGICK_VERSION && ./configure && make && make install
&& yum install -y cairo cairo-devel cairomm-devel libjpeg-turbo-devel pango
pango-devel pangomm pangomm-devel giflib-devel && npm install canvas  
  
CMD ["node", "-v"]  

