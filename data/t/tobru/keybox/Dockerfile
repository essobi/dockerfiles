FROM openjdk:8-slim  
  
ENV KEYBOX_VERSION=2.90.01 \  
KEYBOX_FILENAME=2.90_01 \  
DOCKERIZE_VERSION=0.5.0  
RUN apt-get update && apt-get -y install wget && \  
wget --quiet
https://github.com/skavanagh/KeyBox/releases/download/v${KEYBOX_VERSION}/keybox-
jetty-v${KEYBOX_FILENAME}.tar.gz && \  
wget --quiet
https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-
linux-amd64-v${DOCKERIZE_VERSION}.tar.gz && \  
tar xzf keybox-jetty-v${KEYBOX_FILENAME}.tar.gz -C /opt && \  
tar xzf dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz -C /usr/local/bin
&& \  
mv /opt/KeyBox-jetty /opt/keybox && \  
rm keybox-jetty-v${KEYBOX_FILENAME}.tar.gz dockerize-linux-
amd64-v${DOCKERIZE_VERSION}.tar.gz && \  
apt-get remove --purge -y wget && apt-get -y autoremove && rm -rf
/var/lib/apt/lists/* && \  
# create db directory for later permission update  
mkdir /opt/keybox/jetty/keybox/WEB-INF/classes/keydb && \  
# remove default config - will be written by dockerize on startup  
rm /opt/keybox/jetty/keybox/WEB-INF/classes/KeyBoxConfig.properties && \  
# correct permission for running as non-root (f.e. on OpenShift)  
chgrp -R 0 /opt/keybox && \  
chmod -R g=u /opt/keybox  
  
# persistent data of KeyBox is stored here  
VOLUME /opt/keybox/jetty/keybox/WEB-INF/classes/keydb  
  
# this is the home of KeyBox  
WORKDIR /opt/keybox  
  
# dont run as root  
USER 1001  
# KeyBox listens on 8443 - HTTPS  
EXPOSE 8443  
# KeyBox configuration template for dockerize  
ADD KeyBoxConfig.properties.tpl /opt  
  
# Configure Jetty  
ADD jetty-start.ini /opt/keybox/jetty/start.ini  
  
# Custom Jetty start script  
ADD startKeyBox.sh /opt/keybox/startKeyBox.sh  
  
ENTRYPOINT ["/usr/local/bin/dockerize"]  
CMD ["-template", \  
"/opt/KeyBoxConfig.properties.tpl:/opt/keybox/jetty/keybox/WEB-
INF/classes/KeyBoxConfig.properties", \  
"/opt/keybox/startKeyBox.sh"]  

