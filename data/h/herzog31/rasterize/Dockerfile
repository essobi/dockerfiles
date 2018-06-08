FROM ubuntu:latest  
  
MAINTAINER Mark J. Becker <mjb@marb.ec>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty multiverse" >
/etc/apt/sources.list.d/multiverse.list  
  
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget \  
unzip \  
libicu52 \  
libjpeg8 \  
libwebp5 \  
libfreetype6 \  
libfontconfig \  
ttf-mscorefonts-installer \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget -q --no-check-certificate -O
/tmp/phantomjs-2.0.0-20150528-u1404-x86_64.zip
https://github.com/bprodoehl/phantomjs/releases/download/v2.0.0-20150528/phantomjs-2.0.0-20150528-u1404-x86_64.zip
\  
&& unzip /tmp/phantomjs-2.0.0-20150528-u1404-x86_64.zip -d /tmp \  
&& ln -s /tmp/phantomjs-2.0.0-20150528/bin/phantomjs /usr/bin/phantomjs \  
&& rm /tmp/phantomjs-2.0.0-20150528-u1404-x86_64.zip  
  
RUN mkdir -p /raster-root \  
&& mkdir -p /raster-output  
COPY rasterize.js /raster-root/  
WORKDIR /raster-root  
  
ENTRYPOINT ["phantomjs", "--ignore-ssl-errors=yes", "/raster-
root/rasterize.js"]

