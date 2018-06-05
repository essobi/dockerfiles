# alexindigo/npm-elasticsearch  
FROM elasticsearch:1.4  
MAINTAINER Alex Indigo <iam@alexindigo.com>  
  
ENV NODE_VERSION v0.10.38  
# Install head plugin  
RUN /usr/share/elasticsearch/bin/plugin --install mobz/elasticsearch-head  
  
# Install kopf plugin  
RUN /usr/share/elasticsearch/bin/plugin --install lmenezes/elasticsearch-kopf  
  
# Make log dir as workdir, so java error log files will be available  
# for the mapping outside of the container  
WORKDIR /var/log/elasticsearch  
  
# Add node dev environment  
RUN apt-get update  
RUN apt-get install -y build-essential python git curl  
  
RUN curl -L -s
http://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz -o
/tmp/node-${NODE_VERSION}.tar.gz && \  
cd /tmp/ && \  
tar -xzf ./node-${NODE_VERSION}.tar.gz  
  
RUN cd /tmp/node-${NODE_VERSION} && ./configure && make && make install  
  
RUN rm -rf /tmp/node-${NODE_VERSION}*  
  
# Add pm2, to be on par with alexindigo/node-app image  
RUN npm install -g pm2  
  
# autostart application  
# CMD ["/usr/share/elasticsearch/bin/elasticsearch"]  
CMD ["./autostart"]  

