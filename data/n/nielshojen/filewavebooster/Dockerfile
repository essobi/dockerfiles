FROM centos:centos7  
  
MAINTAINER Niels Højen <niels@hojen.net>  
  
ENV FWBOOSTER_VERSION 12.8.1  
ENV FWBOOSTER_NAME "NewBooster"  
ENV FWBOOSTER_LOCATION "New Branch Office"  
ENV FWBOOSTER_PASSWORD "filewave"  
ENV FWBOOSTER_PORT 20013  
ENV FWBOOSTER_PUBPORT 20003  
ENV FWSERVER1_PORT 20015  
ENV FWSERVER1_ADDR "no.server.set"  
ENV FWSERVER1_SUBSPORT 20005  
ENV FWBOOSTER_SSLLOADER 0  
ENV FWBOOSTER_FREEDISKSPACELIMIT 500  
VOLUME /var/FWBooster  
  
RUN yum -y install wget unzip initscripts  
RUN wget
https://fwdl.filewave.com/$FWBOOSTER_VERSION/FileWave_Linux_$FWBOOSTER_VERSION.zip  
RUN unzip FileWave_Linux_$FWBOOSTER_VERSION.zip  
RUN rm -f fwxserver-$FWBOOSTER_VERSION-1.0.x86_64.rpm  
RUN yum install -y --nogpgcheck fwbooster-$FWBOOSTER_VERSION-1.0.x86_64.rpm  
  
ADD fwbooster.conf /fwbooster.conf  
ADD run.sh /run.sh  
  
EXPOSE 20003  
EXPOSE 20004  
EXPOSE 20013  
EXPOSE 20014  
CMD /bin/bash /run.sh  

