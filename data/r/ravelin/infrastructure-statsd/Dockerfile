############################################################  
# StatsD  
# Based on Phusion Image - https://github.com/phusion/baseimage-docker  
# ENV SUITABILITY: DEVELOPMENT  
############################################################  
  
FROM phusion/baseimage:0.9.15  
  
# Update the default application repository sources list  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install NodeJS  
ADD http://nodejs.org/dist/v0.10.31/node-v0.10.31-linux-x64.tar.gz
/tmp/node.tgz  
RUN mkdir -p /src/node && tar xzf /tmp/node.tgz -C /src/node --strip=1 && rm
-f /tmp/node.tgz  
  
# Install StatsD  
ADD
https://github.com/etsy/statsd/archive/9cf48db0fe9365f9c26ad5623c1e776d0192b601.tar.gz
/tmp/statsd.tgz  
RUN mkdir -p /src/statsd && tar xzf /tmp/statsd.tgz -C /src/statsd --strip=1
&& rm -f /tmp/statsd.tgz  
  
# Confiure StatsD  
ADD ./config.js /src/statsd/config.js  
  
  
#stdout_logfile = /var/log/supervisor/%(program_name)s.log  
#stderr_logfile = /var/log/supervisor/%(program_name)s.log  
  
  
# StatsD UDP port and Management port  
USER root  
EXPOSE 8125/udp  
EXPOSE 8126/tcp  
  
ENTRYPOINT ["/src/node/bin/node", "/src/statsd/stats.js",
"/src/statsd/config.js"]

