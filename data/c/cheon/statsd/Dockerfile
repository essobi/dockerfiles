FROM ubuntu:14.04.3  
MAINTAINER cheon <cheon19950317@gmail.com>  
RUN apt-get update  
RUN apt-get -y install curl git xz-utils  
WORKDIR /opt  
RUN curl -O https://nodejs.org/dist/v6.9.4/node-v6.9.4-linux-x64.tar.xz  
RUN xz -d node-v6.9.4-linux-x64.tar.xz  
RUN tar -xvf node-v6.9.4-linux-x64.tar  
ENV NODE_HOME=/opt/node-v6.9.4-linux-x64  
ENV PATH=$PATH:$NODE_HOME/bin  
ENV NODE_PATH=$NODE_HOME/lib/node_modules  
RUN git clone https://github.com/etsy/statsd.git  
RUN curl https://raw.githubusercontent.com/danslimmon/statsd-opentsdb-
backend/master/statsd-opentsdb-backend/index.js >
/opt/statsd/backends/opentsdb.js  
ADD config.js /opt/statsd/config.js  
EXPOSE 8125  
CMD sed -i "s#localhost#$TSDB_ADDRESS#" /opt/statsd/config.js && node
/opt/statsd/stats.js /opt/statsd/config.js  

