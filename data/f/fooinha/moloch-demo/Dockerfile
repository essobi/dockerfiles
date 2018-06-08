#FROM ubuntu:16.04  
FROM solita/ubuntu-systemd:16.04  
# docker create -t --net bridge --privileged -p 8005:8005 -p 8008:8008 -p
8081:8081 --name moloch fooinha/moloch:latest  
USER root  
RUN apt-get -y update  
  
RUN apt-get -y install \  
less \  
curl \  
ethtool \  
psmisc \  
wget \  
vim \  
libjson-perl \  
libmagic1 \  
libwww-perl \  
libyaml-dev \  
default-jre \  
squid  
  
EXPOSE 3128/tcp  
  
WORKDIR /tmp  
RUN wget https://files.molo.ch/builds/ubuntu-16.04/moloch_1.1.0-1_amd64.deb  
RUN dpkg -i moloch_1.1.0-1_amd64.deb  
  
WORKDIR /data/moloch  
  
ENV MOLOCH_INTERFACE=eth0  
ENV MOLOCH_LOCALELASTICSEARCH=yes  
ENV MOLOCH_PASSWORD=password  
ENV ESHOST localhost  
  
EXPOSE 8005/tcp  
  
COPY configure.sh bin/.  
RUN chmod +x bin/configure.sh  
RUN ./bin/configure.sh  
  
COPY packet-drop-ips.ini etc/.  
RUN cat etc/packet-drop-ips.ini >> etc/config.ini  
  
COPY moloch-bootstrap.sh bin/.  
RUN chmod +x bin/moloch-bootstrap.sh  
COPY moloch-bootstrap.service /etc/systemd/system/.  
RUN systemctl enable elasticsearch.service  
RUN systemctl enable moloch-bootstrap.service  
  
RUN echo "export MOLOCH_LOCALELASTICSEARCH=${MOLOCH_LOCALELASTICSEARCH}" >>
/etc/profile  
RUN echo "export MOLOCH_PASSWORD=${MOLOCH_PASSWORD}" >> /etc/profile  
RUN echo "export ESHOST=${ESHOST}" >> /etc/profile  
  
# Open squid for everyone  
RUN sed -i -e 's/http_access deny all/http_access allow all/'
/etc/squid/squid.conf  
  

