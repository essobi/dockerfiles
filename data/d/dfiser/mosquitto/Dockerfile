FROM debian:jessie-slim  
  
MAINTAINER Daniel Fišer <daniel@fiser.cz>  
  
# install wget  
RUN \  
apt-get update && \  
apt-get install -y wget  
  
# set up the official mosquitto Debian pkg repo  
# https://mosquitto.org/2013/01/mosquitto-debian-repository/  
RUN \  
wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key && \  
apt-key add mosquitto-repo.gpg.key && \  
rm -f mosquitto-repo.gpg.key && \  
wget --output-document=/etc/apt/sources.list.d/mosquitto-jessie.list
http://repo.mosquitto.org/debian/mosquitto-jessie.list && \  
apt-get update && \  
apt-get install -y mosquitto && \  
rm -rf /var/lib/apt/lists/*  
  
# create mosquitto volume dir  
RUN \  
mkdir -p /opt/mosquitto/etc /opt/mosquitto/persistence && \  
chown -R mosquitto:mosquitto /opt/mosquitto  
  
# copy mosquitto config file  
COPY mosquitto.conf /opt/mosquitto/etc/mosquitto.conf  
  
# expose mosquitto dir, incl. logs and persistance files  
VOLUME ["/opt/mosquitto"]  
  
EXPOSE 1883 9001  
ENTRYPOINT ["/usr/sbin/mosquitto"]  
CMD [" --help"]  
  

