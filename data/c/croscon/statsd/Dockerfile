FROM croscon/ubuntu:trusty  
  
RUN apt-get -y update && apt-get -y upgrade && apt-get install git nodejs \  
&& mkdir -p /opt \  
&& cd /opt \  
&& git clone https://github.com/etsy/statsd.git && cd statsd && git checkout
v0.8.0 \  
&& find /var/lib/apt/lists -type f -delete  
ADD devConfig.js /opt/statsd/  
WORKDIR /opt/statsd  
EXPOSE 8125:8125/udp 8126:8126  
ENTRYPOINT /opt/statsd/bin/statsd devConfig.js  
  

