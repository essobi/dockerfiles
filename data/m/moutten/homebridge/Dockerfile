FROM ubuntu:16.04  
LABEL maintainer="Matt Outten <matt@outten.net>"  
  
# Install Supporting Packages  
RUN apt-get -q update && \  
apt-get install -qy curl python && \  
curl -sL https://deb.nodesource.com/setup_4.x | bash - && \  
apt-get -q update && \  
apt-get install -qy \  
build-essential \  
git \  
nodejs \  
libavahi-compat-libdnssd-dev && \  
apt-get -q clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN npm -g install npm@latest-2 && \  
npm install -g homebridge && \  
npm install -g homebridge-indigo && \  
mkdir -p /config && \  
cp /usr/lib/node_modules/homebridge-indigo/sampleconfig.json
/config/config.json  
  
COPY run.sh /run.sh  
  
RUN chmod +x /run.sh && mkdir -p /var/run/dbus  
  
VOLUME /config  
  
CMD ["/run.sh"]  

