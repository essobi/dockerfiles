FROM debian:jessie  
MAINTAINER Tony Arnold <tony@thecocoabots.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update and install the required software  
RUN echo "deb http://www.ubnt.com/downloads/unifi/debian unifi5 ubiquiti" > \  
/etc/apt/sources.list.d/20ubiquiti.list && \  
echo "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen"
> \  
/etc/apt/sources.list.d/21mongodb.list && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" > \  
/etc/apt/sources.list.d/22webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" >
\  
/etc/apt/sources.list.d/23webupd8team-java-src.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50 && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10 && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv EEA14886  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
RUN apt-get -q update && \  
apt-get install -qy --force-yes oracle-java8-installer oracle-java8-set-
default unifi && \  
apt-get -q clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV JAVA8_HOME /usr/lib/jvm/java-8-oracle  
# Install beta version of controller software  
ADD https://dl.ubnt.com/unifi/5.9.4-b647df56b7/unifi_sysvinit_all.deb
/tmp/unifi_sysvinit_all.deb  
RUN dpkg -i /tmp/unifi_sysvinit_all.deb && rm /tmp/unifi_sysvinit_all.deb  
  
# Wipe out auto-generated data  
RUN rm -rf /usr/lib/unifi/data  
# Expose ports, and set working directory  
EXPOSE 3478/udp 8080/tcp 8081/tcp 8443/tcp 8843/tcp 8880/tcp  
VOLUME /usr/lib/unifi/data  
WORKDIR /usr/lib/unifi/data  
# Start the UniFi controller process  
ENTRYPOINT ["/usr/lib/jvm/java-8-oracle/jre/bin/java", "-Xmx1024M", "-jar",
"/usr/lib/unifi/lib/ace.jar"]  
CMD ["start"]  

