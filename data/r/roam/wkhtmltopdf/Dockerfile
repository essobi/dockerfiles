# Use Ubuntu because of its better font hinting defaults  
FROM ubuntu:12.04  
MAINTAINER Kevin Wetzels <kevin@roam.be>  
# Add a local copy (because Sourceforge)  
ADD wkhtmltox-0.12.2.1_linux-precise-amd64.deb .  
# Install prerequisites and common fonts  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ precise multiverse' >>
/etc/apt/sources.list && \  
echo 'deb-src http://us.archive.ubuntu.com/ubuntu/ precise multiverse' >>
/etc/apt/sources.list && \  
$(echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections) && \  
apt-get update && \  
apt-get install -y xorg libssl-dev libxrender-dev libjpeg8-dev libjpeg8
fontconfig ttf-mscorefonts-installer xfonts-75dpi && \  
dpkg -i wkhtmltox-0.12.2.1_linux-precise-amd64.deb  
ENTRYPOINT ["/usr/local/bin/wkhtmltopdf"]  
CMD ["-h"]  

