FROM debian:latest  
MAINTAINER Ventz Petkov <ventz@vpetkov.net>  
  
VOLUME ["/usr/lib/unifi/data"]  
EXPOSE 8080/tcp 8443/tcp 8880/tcp 8843/tcp 3478/udp 8081/tcp 8082/tcp  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -qy install gnupg openjdk-8-jre-headless ca-certificates-java && \  
echo "deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti" > \  
/etc/apt/sources.list.d/100-ubnt-unifi.list && \  
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2
multiverse" > \  
/etc/apt/sources.list.d/mongodb-org-3.2.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv 06E85760C0A52C50 && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
#echo "deb http://http.debian.net/debian jessie-backports main" >>
/etc/apt/sources.list && \  
RUN apt-get update && \  
apt-get install -qy unifi && \  
apt-get -qy clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/lib/unifi  
  
ENTRYPOINT ["/usr/bin/java", "-Xmx1024M", "-jar",
"/usr/lib/unifi/lib/ace.jar"]  
CMD ["start"]  

