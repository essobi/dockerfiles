FROM openjdk:8-jdk  
  
MAINTAINER André Santos <dre.santos@gmail.com>  
  
# working directory for gatling  
WORKDIR /opt  
  
# gating version  
ENV GATLING_VERSION 2.2.3  
# create directory for gatling install  
RUN mkdir -p gatling  
  
# install gatling  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
mkdir -p /tmp/downloads && \  
wget -q -O /tmp/downloads/gatling-$GATLING_VERSION.zip \  
https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-
highcharts-bundle/$GATLING_VERSION/gatling-charts-highcharts-
bundle-$GATLING_VERSION-bundle.zip && \  
mkdir -p /tmp/archive && cd /tmp/archive && \  
unzip /tmp/downloads/gatling-$GATLING_VERSION.zip && \  
mv /tmp/archive/gatling-charts-highcharts-bundle-$GATLING_VERSION/*
/opt/gatling/ && \  
rm -rf /tmp/*  
  
# change context to gatling directory  
WORKDIR /opt/gatling  
  
RUN ln -s /opt/gatling/bin/gatling.sh /opt/gatling/bin/gatling && \  
ln -s /opt/gatling/bin/recorder.sh /opt/gatling/bin/recorder  
  
# set directories below to be mountable from host  
VOLUME ["/opt/gatling/conf", "/opt/gatling/results", "/opt/gatling/user-
files"]  
  
# set environment variables  
ENV PATH
/opt/gatling/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ENV GATLING_HOME /opt/gatling  
  
CMD ["/bin/bash"]  
  

