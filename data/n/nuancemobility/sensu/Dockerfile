FROM nuancemobility/ubuntu-base:14.04  
MAINTAINER Brice Argenson <brice.argenson@nuance.com>  
  
# Install Redis  
RUN apt-get install -y redis-server  
  
# Install Sensu  
RUN curl http://repos.sensuapp.org/apt/pubkey.gpg | apt-key add \- && \  
echo "deb http://repos.sensuapp.org/apt sensu main" >
/etc/apt/sources.list.d/sensu.list && \  
apt-get -y update && apt-get install -y sensu  
  
# Install and configure WizardVan  
RUN apt-get install -y git && \  
git clone http://github.com/opower/sensu-metrics-relay.git && \  
cp -R sensu-metrics-relay/lib/sensu/extensions/* /etc/sensu/extensions  
  
  
#Install snmp utilities  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse\n" >>
/etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu trusty multiverse\n" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get -y install libsnmp-base snmp-mibs-downloader snmp  
  
  
# Install Sensu Plugins  
RUN apt-get -y update && apt-get install -y ruby ruby-dev build-essential && \  
gem install mail --no-ri \--no-rdoc -v 2.5.4 && \  
gem install json --no-ri \--no-rdoc -v 1.8.3 && \  
gem install sensu-plugin --no-ri \--no-rdoc -v 1.2.0  
  
  
VOLUME /etc/sensu/conf.d  
VOLUME /etc/sensu/handlers  
  
COPY supervisor /etc/supervisor/conf.d  

