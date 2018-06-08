FROM node:0.10  
# grab gosu for easy step-down from root  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN arch="$(dpkg --print-architecture)" \  
&& set -x \  
&& curl -o /usr/local/bin/gosu -fSL
"https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch" \  
&& curl -o /usr/local/bin/gosu.asc -fSL
"https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch.asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r statsd && useradd -r -g statsd statsd  
  
RUN npm install -g statsd@0.7.2  
  
# Setup config  
COPY statsd-config.js /opt/statsd/config.js  
  
COPY docker-entrypoint.sh /  
  
EXPOSE 8125/udp  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["statsd", "/opt/statsd/config.js"]

