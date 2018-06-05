FROM ubuntu:16.04  
ENV SERVERPORT="80" \  
VERSION="4.2.1" \  
DEBCONF_NONINTERACTIVE_SEEN="true" \  
DEBIAN_FRONTEND="noninteractive"  
WORKDIR /]  
RUN apt-get update && apt-get -y upgrade  
  
RUN apt-get -y install software-properties-common netcat && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y \  
oracle-java8-installer \  
oracle-java8-set-default && \  
usermod -u 99 nobody && \  
usermod -g 100 nobody  
  
RUN apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /ha-bridge-scripts  
ADD src/* ./  
  
WORKDIR /config  
RUN wget -q -O ./ha-bridge.jar https://github.com/bwssytems/ha-
bridge/releases/download/v"$VERSION"/ha-bridge-"$VERSION".jar && \  
mkdir /config/startup-config/  
  
RUN setcap 'cap_net_bind_service=+ep' /usr/lib/jvm/java-8-oracle/jre/bin/java  
RUN chmod -R 0775 /ha-bridge-scripts && \  
chmod -R 0776 /config && \  
chown -R nobody:users /config  
  
USER nobody  
VOLUME ["/config/data"]  
ENTRYPOINT /ha-bridge-scripts/new_entrypoint  

