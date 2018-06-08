FROM node:6  
  
# Home directory for Node-RED application source code.  
RUN mkdir -p /usr/src/node-red  
  
# User data directory, contains flows, config and nodes.  
USER root  
  
RUN mkdir -p /data/ssh  
RUN mkdir /settings  
  
# Install logstash dependencies  
WORKDIR /settings  
RUN npm install bunyan bunyan-logstash-tcp json-stringify-unsafe  
  
WORKDIR /usr/src/node-red  
  
# Create SSH key (key will be stored on volume)  
COPY ssh/id_rsa /root/.ssh/  
COPY ssh/id_rsa.pub /root/.ssh/  
COPY ssh/known_hosts /root/.ssh/  
RUN chmod 400 /root/.ssh/id_rsa \  
&& chmod 400 /root/.ssh/id_rsa.pub  
  
# Install Node-RED  
RUN npm install node-red@0.17.4  
  
# Set npm registry  
ENV NPM_REGISTRY=http://catalog.shared.sinapse-ps.com:9100  
  
  
WORKDIR /data  
  
# git user  
ENV GIT_USER botsinapse  
ENV GIT_EMAIL bot.sinapse@soaexpert.com.br  
RUN git config \--global user.name $GIT_USER  
RUN git config \--global user.email $GIT_EMAIL  
# Copy custom settings.js  
COPY settings.js /settings/  
COPY favicon.ico logo_sin.gif logo_porto.png style.css /settings/  
COPY entrypoint.sh /settings/  
COPY settings.js /root/.node-red/  
  
RUN cd /root/.node-red/ && npm install bunyan bunyan-logstash-tcp json-
stringify-unsafe  
  
ENV MAX_MEMORY=1G  
ENV SUBFLOWS_HOST=catalog.shared.sinapse-ps.com:9003  
ENV BUNYAN_HOST=logstash  
ENV BUNYAN_PORT=9998  
ENV CATALOGUE_URL=http://catalog.shared.sinapse-ps.com:9101/catalogue.json  
ENV ENVIRONMENT=prod  
# User configuration directory volume  
ENV PORT 1880  
EXPOSE $PORT  
# Environment variable holding file path for flows configuration  
ENV FLOWS=flows.json  
  
RUN chmod +x /settings/entrypoint.sh && \  
chown root /settings/entrypoint.sh && \  
chmod 777 /settings/entrypoint.sh  
  
  
CMD ../settings/entrypoint.sh

