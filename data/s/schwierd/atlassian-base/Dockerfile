FROM ubuntu:wily  
MAINTAINER Daniel Schwierzeck <daniel.schwierzeck@gmail.com>  
  
# Fix time zone  
RUN echo 'Europe/Berlin' > /etc/timezone && \  
cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime  
  
# prepare APT  
ENV DEBIAN_FRONTEND noninteractive  
  
# install tools and libraries  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
curl \  
ca-certificates \  
libtcnative-1  
  
# install Oracle Java SE Development Kit 8u74  
RUN mkdir -p /opt/jdk && \  
curl -sSL --cookie oraclelicense=accept-securebackup-cookie \  
-H 'Host: download.oracle.com' \  
-H 'User-Agent: Mozilla/5.0 (compatible)' \  
-H 'Referer: http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html' \  
-H 'Connection: keep-alive' \  
http://download.oracle.com/otn-pub/java/jdk/8u74-b02/jdk-8u74-linux-x64.tar.gz
\  
| tar -xz --strip=1 -C /opt/jdk/ && \  
update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 && \  
update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100 && \  
java -version  
  
# clean up APT  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

