FROM debian:jessie  
MAINTAINER madsonic (support@madsonic.org)  
  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
# Madsonic Package Information  
ENV PKG_NAME madsonic  
ENV PKG_VER 6.2  
ENV PKG_BUILD 9040  
ENV PKG_DATE 20161208  
# Use init system  
CMD ["/sbin/my_init"]  
  
# Fix ids  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
  
# Add Oracle Java8 Repo  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
\  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections  
  
# Install apt packages  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
locales \  
oracle-java8-installer \  
oracle-java8-set-default \  
unzip \  
wget  
  
# download madsonic  
RUN mkdir -p /var/madsonic/transcode \  
&& wget -O /var/madsonic/madsonic.zip
http://www.madsonic.org/download/${PKG_VER}/${PKG_DATE}_${PKG_NAME}-${PKG_VER}.${PKG_BUILD}-standalone.zip
\  
&& wget -O /var/madsonic/transcode.zip
http://www.madsonic.org/download/transcode/${PKG_DATE}_${PKG_NAME}-transcode-
linux-x64.zip  
  
# Install Madsonic  
RUN mkdir -p /var/madsonic/transcode \  
&& unzip /var/madsonic/madsonic.zip -d /var/madsonic \  
&& unzip /var/madsonic/transcode.zip -d /var/madsonic \  
&& chown -R nobody:users /var/madsonic \  
&& chmod -R 755 /var/madsonic \  
&& rm /var/madsonic/madsonic.zip \  
&& rm /var/madsonic/transcode.zip  
  
# Force Madsonic to run in foreground  
RUN sed -i 's/-jar madsonic-booter.jar > \${LOG} 2>\&1 \&/-jar madsonic-
booter.jar > \${LOG} 2>\&1/g' /var/madsonic/madsonic.sh  
  
# apt clean  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
# Set Locale env  
ENV LANG C.UTF-8  
# default http https port  
EXPOSE 4040 4050  
# App configuration  
VOLUME /config  
  
# media directory  
VOLUME /media  
  
# Copy start.sh script  
ADD ./start.sh /start.sh  
RUN chmod +x /start.sh  
RUN chown -R nobody:users /start.sh  
  
# run App as user  
USER nobody  
ENTRYPOINT ["/start.sh"]  

