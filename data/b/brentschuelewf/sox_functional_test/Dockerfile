# Dart SDK, Sauce Connect, Docker Compose  
FROM ubuntu:trusty  
  
MAINTAINER Brent Schuele <brent.schuele@workiva.com>  
  
LABEL Description="This image contains the Dart SDK, Sauce Connect, and Docker
Compose"  
  
ENV CHANNEL stable  
ENV SDK_VERSION 1.15.0  
ENV ARCHIVE_URL https://storage.googleapis.com/dart-
archive/channels/$CHANNEL/release/$SDK_VERSION  
ENV PATH $PATH:/usr/lib/dart/bin  
ENV SC_VERSION 4.3.16  
ENV COMPOSE_VERSION 1.7.1  
RUN apt-get update && apt-get install -y \  
git \  
ssh \  
unzip \  
wget \  
curl \  
&& apt-get clean  
  
RUN wget $ARCHIVE_URL/sdk/dartsdk-linux-x64-release.zip \  
&& unzip dartsdk-linux-x64-release.zip \  
&& cp dart-sdk/* /usr/local -r \  
&& rm -rf dartsdk-linux-x64-release.zip  
  
RUN wget -O ./sauce-connect.tar.gz
https://saucelabs.com/downloads/sc-$SC_VERSION-linux.tar.gz \  
&& tar -zxvf sauce-connect.tar.gz \  
&& mv sc-$SC_VERSION-linux/bin/sc /usr/local/bin \  
&& rm -rf sauce-connect.tar.gz \  
&& rm -rf $SC_VERSION-linux/  
  
RUN curl -fsSL https://get.docker.com/ | sh \  
&& curl -L
https://github.com/docker/compose/releases/download/$COMPOSE_VERSION/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  

