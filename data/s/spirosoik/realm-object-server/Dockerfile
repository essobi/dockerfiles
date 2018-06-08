FROM ubuntu:16.04  
MAINTAINER Spiros I. Economakis <spiros.oikonomakis@gmail.com>  
  
EXPOSE 9080  
RUN apt-get update && \  
apt-get -y install curl  
  
# Setup Realm's PackageCloud repository  
RUN curl -s
https://packagecloud.io/install/repositories/realm/realm/script.deb.sh | bash  
  
# Install the Realm Object Server  
RUN apt-get -y install realm-object-server-de  
  
# Enable and start the service  
RUN systemctl enable realm-object-server  
  
VOLUME /etc/realm/  
  
# Start the service  
CMD /usr/bin/realm-object-server -c /etc/realm/configuration.yml

