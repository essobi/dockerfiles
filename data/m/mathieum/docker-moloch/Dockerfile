FROM ubuntu:16.04  
MAINTAINER Mathieu Monin - https://github.com/mathiem  
  
RUN apt-get -qq update && \  
apt-get -yq install software-properties-common && \  
add-apt-repository ppa:openjdk-r/ppa && \  
apt-get -qq update && \  
apt-get install -yq wget curl libpcre3-dev uuid-dev libmagic-dev pkg-config
g++ flex bison zlib1g-dev libffi-dev gettext libgeoip-dev make libjson-perl
libbz2-dev libwww-perl libpng-dev xz-utils libffi-dev python git openjdk-7-jdk
libssl-dev libyaml-dev ethtool && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Declare args  
ARG MOLOCH_VERSION=0.50.0-1_amd64  
ARG UBUNTU_VERSION=16.04  
ARG ES_HOST=elasticsearch  
ARG ES_PORT=9200  
ARG MOLOCH_PASSWORD=admin  
ARG MOLOCH_INTERFACE=eth0  
ARG CAPTURE=on  
ARG VIEWER=on  
  
# Declare envs vars for each arg  
ENV ES_HOST $ES_HOST  
ENV ES_PORT $ES_PORT  
ENV MOLOCH_LOCALELASTICSEARCH no  
ENV MOLOCH_ELASTICSEARCH "http://"$ES_HOST":"$ES_PORT  
ENV MOLOCH_INTERFACE $MOLOCH_INTERFACE  
ENV MOLOCH_PASSWORD $MOLOCH_PASSWORD  
ENV MOLOCH_ADMIN_PASSWORD $MOLOCH_PASSWORD  
ENV MOLOCHDIR "/data/moloch"  
ENV CAPTURE $CAPTURE  
ENV VIEWER $VIEWER  
  
RUN mkdir -p /data  
RUN cd /data && curl -C - -O
"https://files.molo.ch/builds/ubuntu-"$UBUNTU_VERSION"/moloch_"$MOLOCH_VERSION".deb"  
RUN cd /data && dpkg -i "moloch_"$MOLOCH_VERSION".deb"  
  
# add scripts  
ADD /scripts /data/  
RUN chmod 755 /data/startmoloch.sh  
  
VOLUME ["/data/pcap", "/data/moloch/logs"]  
EXPOSE 8005  
WORKDIR /data/moloch  
  
ENTRYPOINT ["/data/startmoloch.sh"]  
  

