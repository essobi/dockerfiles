FROM ubuntu:xenial  
MAINTAINER Chris Smith <chris87@gmail.com>  
  
ARG url=https://www.ubnt.com/downloads/unifi/5.7.23/unifi_sysvinit_all.deb  
  
RUN \  
apt-get update && \  
apt-get -y install \  
binutils \  
curl \  
jsvc \  
mongodb-server \  
openjdk-8-jre-headless \  
software-properties-common  
  
RUN curl -L -o unifi_sysvinit_all.deb $url && \  
dpkg --install unifi_sysvinit_all.deb && \  
rm unifi_sysvinit_all.deb && \  
ln -s /var/lib/unifi /usr/lib/unifi/data  
  
EXPOSE 8080 8443 8843 8880  
VOLUME ["/var/lib/unifi"]  
  
WORKDIR /var/lib/unifi  
  
CMD ["/usr/bin/java", "-Xmx1024M", "-jar", "/usr/lib/unifi/lib/ace.jar",
"start"]  
  

