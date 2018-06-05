FROM centos:7  
MAINTAINER Karl Stoney <me@karlstoney.com>  
  
# Get dependencies  
RUN yum -y -q install curl wget gettext patch  
  
# Get nodejs repos  
RUN curl --silent --location https://rpm.nodesource.com/setup_6.x | bash -  
  
# Install nodejs, max currently supported is 6.9.0  
RUN yum -y -q install nodejs-6.9.* gcc-c++ make git bzip2 unzip && \  
yum -y -q clean all  
  
# Configuration  
ENV GHOST_CONFIG /data/config.js  
ENV GHOST_HOME /var/www/ghost  
ENV GHOST_VERSION 0.11.10  
# Setup www-data user  
RUN groupadd www-data && \  
useradd -r -g www-data www-data  
  
RUN mkdir -p /var/www && \  
mkdir -p /home/www-data && \  
mkdir -p /data && \  
chown -R www-data:www-data /var/www && \  
chown -R www-data:www-data /home/www-data && \  
chown -R www-data:www-data /data  
  
USER www-data  
  
# Install Ghost  
RUN cd /tmp && \  
curl -L --silent
https://github.com/TryGhost/Ghost/releases/download/$GHOST_VERSION/Ghost-$GHOST_VERSION.zip
-o ghost.zip && \  
unzip -uo ghost.zip -d $GHOST_HOME &>/dev/null && \  
rm -f ghost.zip && \  
cd $GHOST_HOME && \  
npm install --production  
  
RUN cd $GHOST_HOME && \  
ln -sf config.js /data/config.js && \  
cd content && \  
rm -rf data && \  
rm -rf images && \  
ln -sf /data/data data && \  
ln -sf /data/images images  
  
USER root  
  
WORKDIR $GHOST_HOME  
VOLUME /data  
  
EXPOSE 2368  
RUN mkdir -p /usr/local/etc/ghost/patches  
COPY patches/ /usr/local/etc/ghost/patches/  
COPY config.js.default /usr/local/etc/ghost/  
COPY run.sh /usr/local/bin/run.sh  
CMD ["/usr/local/bin/run.sh"]  

