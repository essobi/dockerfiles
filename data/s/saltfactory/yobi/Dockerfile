FROM debian:jessie  
MAINTAINER pokev25 <pokev25@gmail.com>  
  
LABEL Description="This image is used to start the yona-1.0.2"
Vendor="pokev25" Version="1.0.2"  
  
## replace debian mirror with ftp.daum.net in Korea  
RUN cd /etc/apt && \  
sed -i 's/httpredir.debian.org/ftp.daum.net/g' sources.list  
  
## install Oracle Java 8 and clean up installation files  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer oracle-java8-set-default  
  
## install extra package  
RUN apt-get install -y unzip  
  
## Timezone  
RUN echo "Asia/Seoul" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
## remove cache  
RUN rm -rf /var/cache/oracle-jdk8-installer && apt-get clean && rm -rf
/var/lib/apt/lists/*  
  
## add yona user  
RUN useradd -m -d /yona -s /bin/bash -U yona  
RUN mkdir /yona/downloads  
  
## install yona  
RUN cd /yona/downloads; \  
wget https://github.com/yona-
projects/yona/releases/download/v1.0.2/yona-v1.0.2-bin.zip && \  
unzip -d /yona/release yona-v1.0.2-bin.zip && \  
rm -f yona-v1.0.2-bin.zip  
  
## set environment variables  
ENV YONA_HOME "/yona/home"  
ENV JAVA_OPTS "-Xmx2048m -Xms2048m"  
## add entrypoints  
ADD ./entrypoints /yona/entrypoints  
RUN chmod +x /yona/entrypoints/*.sh  
  
## yona home directory mount point from host to docker container  
VOLUME ["/yona/source", "/yona/home"]  
WORKDIR ["/yona"]  
  
## yona service port expose from docker container to host  
EXPOSE 9000  
## run yona command  
ENTRYPOINT ["/yona/entrypoints/bootstrap.sh"]  

