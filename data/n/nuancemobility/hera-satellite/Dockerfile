FROM nuancemobility/sensu-client  
MAINTAINER sspcm <mobility-sspcm@nuance.com>  
  
  
COPY docker-entrypoint.sh /  
  
# Configure Sensu with whatever your checks require  
#RUN apt-get install -y ruby zlib1g-dev ruby-dev build-essential git
libsmi2ldbl && \  
# gem install net-ping sensu-plugin snmp nokogiri nori rest-client colorize
--no-ri --no-rdoc && i  
# Add source list so we can get snmp-mibs  
RUN echo 'deb http://archive.ubuntu.com/ubuntu/ trusty main multiverse' >>
/etc/apt/sources.list  
  
# Update apt  
RUN apt-get update -y  
  
# Configure Sensu for plugin dependencies  
RUN apt-get install -y ruby build-essential  
  
# Install Python plugin dependencies  
RUN apt-get install -y python3-pip && pip3 install -U selenium && pip3 install
requests  
  
# Install Nagios plugins  
RUN apt-get -y install nagios-plugins  
  
# Install SNMP libraries  
RUN apt-get -y install snmp snmp-mibs-downloader  
  
# Install PhantomJS  
RUN apt-get install -y chrpath libssl-dev libxft-dev libfreetype6
libfreetype6-dev libfontconfig libfontconfig1-dev nodejs-legacy nodejs npm &&
\  
npm install phantomjs && mv /node_modules/phantomjs /usr/local/share && ln -sf
/usr/local/share/phantomjs/bin/phantomjs /usr/local/bin/  
  
# Install diagnostic tools  
RUN gem install sensu-plugin vmstat sys sys-filesystem  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["start"]  

