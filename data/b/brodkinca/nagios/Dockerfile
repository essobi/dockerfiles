FROM jasonrivers/nagios:latest  
  
MAINTAINER Brodkin CyberArts  
  
# UNATTENDED INSTALLATION  
ENV DEBIAN_FRONTEND noninteractive  
  
# CONFIGURE PHP TIME ZONE  
ENV TZ "US/Pacific"  
RUN apt-get update \  
&& apt-get install -y heirloom-mailx python-pip \  
&& pip install -U unifi \  
&& pip install -U speedtest-cli \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false  

