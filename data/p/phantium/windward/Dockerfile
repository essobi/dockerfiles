FROM ubuntu:14.04  
MAINTAINER Phantium  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV WWPORT 5127  
ENV WWNAME "Windward Docker Server"  
ENV WWORLD "World"  
ENV WWPUB "1"  
RUN apt-get update \  
&& apt-get -y install wget mono-runtime libmono2.0-cil unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean \  
&& mkdir -p /data/windward/homedir \  
&& useradd -d /data/windward/homedir -s /bin/bash --uid 1000 windward \  
&& chown windward: /data/windward  
  
EXPOSE 5127  
ADD windward.sh /usr/local/bin/windward  
  
USER windward  
VOLUME /data/windward  
WORKDIR /data/windward  
CMD ["windward"]  

