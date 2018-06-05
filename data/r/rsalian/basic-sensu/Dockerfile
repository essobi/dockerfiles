FROM nuancemobility/ubuntu-base:14.04  
MAINTAINER Rajesh Salian <rajesh.salian@nuance.com>  
  
# Install Redis  
RUN apt-get install -y redis-server  
  
# Install Sensu  
RUN curl http://repos.sensuapp.org/apt/pubkey.gpg | apt-key add - && \  
echo "deb http://repos.sensuapp.org/apt sensu main" >
/etc/apt/sources.list.d/sensu.list && \  
apt-get -y update && apt-get install -y sensu  
  
# Install Sensu Plugins  
RUN apt-get install -y ruby ruby-dev build-essential && \  
gem install mail --no-ri --no-rdoc -v 2.5.4 && \  
gem install json --no-ri --no-rdoc -v 1.8.3 && \  
gem install sensu-plugin --no-ri --no-rdoc -v 1.2.0  
  
VOLUME /etc/sensu/conf.d  
VOLUME /etc/sensu/handlers  
  
COPY supervisor /etc/supervisor/conf.d  

