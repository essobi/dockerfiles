FROM node:7.7.1-slim  
MAINTAINER Marius Podwyszynski <marius.pod@gmail.com>  
  
RUN mkdir -p /app && \  
cd /app && \  
curl -L https://github.com/etsy/statsd/tarball/master | tar -xz && \  
mv etsy-statsd-* statsd && \  
apt-get update && apt-get install -y git autoconf build-essential  
  
ENV UREDIR_PORT 8125  
RUN git clone https://github.com/mariuspod/uredir.git /app/uredir-code && \  
cd /app/uredir-code && \  
ls -alrt && \  
./autogen.sh && \  
./configure && \  
make && \  
mv /app/uredir-code/uredir /app/ && \  
rm -fr /app/uredir-code  
  
ENV ES_CONFIG_URL https://raw.githubusercontent.com/mariuspod/statsd-
elasticsearch/master/config.js  
RUN npm install git://github.com/mariuspod/statsd-elasticsearch-backend.git &&
\  
curl -L -k $ES_CONFIG_URL -o /app/elasticsearch-config.js && \  
sed -i 's/port: 8125/port: 8135/g' /app/elasticsearch-config.js  
  
RUN apt-get remove -y git && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATTERNS "es.=127.0.0.1:8135"  
ADD files/startup.sh /app/  
RUN chmod +x /app/startup.sh  
CMD "/app/startup.sh"  

