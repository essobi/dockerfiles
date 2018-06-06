FROM java:7  
MAINTAINER Jordan Brough <jtbrough@icloud.com>  
  
VOLUME ["/var/lib/unifi"]  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Run updates and upgrades  
RUN apt-get -q update && \  
apt-get -q upgrade -y && \  
apt-get -q dist-upgrade -y && \  
apt-get -q clean  
  
# Install common packages  
RUN apt-get -y install curl software-properties-common binutils mongodb-server
jsvc  
  
# Install UniFi 4.6.6  
RUN curl -L -o unifi_sysvinit_all.deb
https://www.ubnt.com/downloads/unifi/4.6.6-bec4a09/unifi_sysvinit_all.deb  
RUN dpkg --install unifi_sysvinit_all.deb  
  
# Cleanup  
RUN rm -rf /var/lib/unifi/* && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8080/tcp 8081/tcp 8443/tcp 8843/tcp 8880/tcp 3478/udp  
  
WORKDIR /var/lib/unifi  
  
CMD ["/usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java", "-Xmx1024M", "-jar",
"/usr/lib/unifi/lib/ace.jar", "start"]  

