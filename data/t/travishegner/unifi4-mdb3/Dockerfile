FROM ubuntu:14.04  
MAINTAINER Travis Hegner <travis.hegner@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV JSVC_EXTRA_OPTS "-user nobody"  
  
RUN \  
mkdir -p /usr/lib/unifi/work && \  
mkdir -p /var/lib/unifi && \  
mkdir -p /var/log/unifi && \  
mkdir -p /var/run/unifi && \  
chown -R nobody:nogroup /usr/lib/unifi/work && \  
chown -R nobody:nogroup /var/lib/unifi && \  
chown -R nobody:nogroup /var/log/unifi && \  
chown -R nobody:nogroup /var/run/unifi  
  
VOLUME ["/var/lib/unifi", "/var/log/unifi", "/var/run/unifi",
"/usr/lib/unifi/work"]  
  
RUN \  
echo "deb http://www.ubnt.com/downloads/unifi/debian unifi4 ubiquiti" >
/etc/apt/sources.list.d/20ubiquiti.list && \  
echo "deb http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.2
multiverse" > /etc/apt/sources.list.d/mongodb-org-3.2.list && \  
#unifi key  
apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50 && \  
#mongodb key  
apt-key adv --keyserver keyserver.ubuntu.com --recv EA312927 && \  
apt-get -q update && \  
apt-get install -qy --force-yes mongodb-org binutils openjdk-7-jre-headless
jsvc && \  
apt-get download unifi && \  
dpkg -i --force-depends unifi*.deb && \  
service unifi stop && \  
apt-get -q clean && \  
rm -rf unifi*.deb && \  
rm -rf /var/lib/apt/lists/*  
  
ADD init.sh /init.sh  
RUN chown nobody:nogroup /init.sh  
  
EXPOSE 8080/tcp 8081/tcp 8443/tcp 8843/tcp 8880/tcp 3478/udp  
  
USER nobody  
  
WORKDIR /var/lib/unifi  
  
ENTRYPOINT ["/bin/bash", "/init.sh"]  

