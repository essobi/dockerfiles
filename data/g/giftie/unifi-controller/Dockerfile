# docker run -d -p 2222:22 -p 8080:8080 -p 8443:8443 -p 27117:27117 -p
10001:10001 -p 8081:8081 -p 3478:3478 -p 8843:8843 -p 8880:8880 -v
/mnt/cache/appdata/unifi:/usr/lib/unifi/data --name unifi giftie/unifi-
controller  
# build docker image to run the unifi controller  
#  
# the unifi contoller is used to admin ubunquty wifi access points  
#  
FROM phusion/baseimage:0.9.11  
MAINTAINER giftie giftie61@hotmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# this forces dpkg not to call sync() after package extraction and speeds up
install  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
# we don't need and apt cache in a container  
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
  
RUN mkdir -p /usr/lib/unifi/data && touch /usr/lib/unifi/data/.unifidatadir  
  
RUN apt-get update -q -y  
RUN apt-get install -q -y apt-utils lsb-release curl wget rsync  
RUN apt-get update  
  
# add ubiquity repo + key  
RUN echo "deb http://www.ubnt.com/downloads/unifi/distros/deb/ubuntu ubuntu
ubiquiti" > /etc/apt/sources.list.d/ubiquity.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50 && apt-get update
-q -y && apt-get install -q -y unifi-rapid  
  
VOLUME /usr/lib/unifi/data  
EXPOSE 3478 8080 8081 8443 8843 8880 10001 27117  
WORKDIR /usr/lib/unifi  
  
CMD ["/usr/lib/jvm/java-6-openjdk-amd64/jre/bin/java", "-Xmx1024M", "-jar",
"/usr/lib/unifi/lib/ace.jar", "start"]  

