FROM ubuntu:16.04  
# Madsonic Package Information  
ENV LANG en_US.utf8  
  
# Install Apt Packages  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
locales \  
default-jre-headless \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
  
# Madsonic Package Information  
ENV PKG_NAME madsonic  
ENV PKG_VER 6.3  
ENV PKG_BUILD 9540  
ENV PKG_DATE 20170703  
ENV DEB_NAME ${PKG_DATE}_${PKG_NAME}-${PKG_VER}.${PKG_BUILD}.deb  
RUN wget http://madsonic.org/download/${PKG_VER}/${DEB_NAME}  
RUN dpkg -i ${DEB_NAME}  
  
# Create hardlinks to the transcoding binaries.  
# This way we can mount a volume over /var/madsonic.  
# <host-dir>/var/madsonic/transcode/ffmpeg -> /usr/local/bin/ffmpeg  
RUN ln /var/madsonic/transcode/ffmpeg /usr/local/bin  
  
VOLUME /var/madsonic  
VOLUME /config  
VOLUME /media  
  
EXPOSE 4040  
EXPOSE 4050  
ADD ./start.sh /start.sh  
RUN chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  

