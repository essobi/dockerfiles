FROM nuancemobility/ubuntu-base:14.04  
MAINTAINER Rajesh Salian <rajesh.salian@nuance.com>  
  
# Install Sensu  
RUN curl http://repos.sensuapp.org/apt/pubkey.gpg | apt-key add - && \  
echo "deb http://repos.sensuapp.org/apt sensu main" >
/etc/apt/sources.list.d/sensu.list && \  
apt-get -y update && \  
apt-get install -y sensu  
  
# Configure Sensu for plugin dependencies  
RUN apt-get install -y ruby build-essential  
  
# Install Python plugin dependencies  
RUN apt-get install -y python3-pip && pip3 install -U selenium && pip3 install
requests  
  
# Install Nagios plugins  
RUN apt-get -y install nagios-plugins  
  
# Install PhantomJS  
RUN apt-get install -y chrpath libssl-dev libxft-dev libfreetype6
libfreetype6-dev libfontconfig1 && \  
libfontconfig1-dev nodejs-legacy nodejs npm && npm install phantomjs && \  
mv /node_modules/phantomjs /usr/local/share && ln -sf
/usr/local/share/phantomjs/bin/phantomjs /usr/local/bin/  
  
COPY docker-entrypoint.sh /  
VOLUME /etc/sensu/conf.d  
VOLUME /etc/sensu/plugins  
VOLUME /etc/sensu/mib  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["start"]  

