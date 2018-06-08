# Originally taken from Johannes Mitlmeier's dockerfile [jojomi/stats]  
# with the addition of version locking etsy/statsd releases  
FROM debian:latest  
  
MAINTAINER Oded Messer <odedm@iguaz.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get --yes update && \  
apt-get --yes dist-upgrade  
  
RUN apt-get --yes install curl && \  
curl -sL https://deb.nodesource.com/setup | bash - && \  
apt-get --yes install nodejs=0.10.48-1nodesource1~jessie1 && \  
apt-get --yes purge curl  
  
ADD https://github.com/etsy/statsd/archive/v0.8.0.tar.gz /tmp/statsd.tar.gz  
  
RUN mkdir -p /src/statsd && tar -xzvf /tmp/statsd.tar.gz --strip-components=1
-C /src/statsd && \  
rm /tmp/statsd.tar.gz  
  
COPY config.js /etc/statsd/config.js  
  
EXPOSE 8125/udp  
  
CMD ["node", "/src/statsd/stats.js", "/etc/statsd/config.js"]  

