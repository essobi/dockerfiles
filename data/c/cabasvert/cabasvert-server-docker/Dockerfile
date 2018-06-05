FROM node:8.9.4-alpine  
  
ENV SERVER_VERSION 0.2.1  
ENV CLIENT_VERSION 0.2.6  
ENV SERVER_CONFIG_FILE /usr/src/app/config.json  
  
ENV SERVER_ARCHIVE cabasvert-node-${SERVER_VERSION}.tgz  
ENV SERVER_URL https://github.com/cabasvert/cabasvert-
server/releases/download/v${SERVER_VERSION}/${SERVER_ARCHIVE}  
ENV CLIENT_ARCHIVE cabasvert-client-browser-${CLIENT_VERSION}.tar.gz  
ENV CLIENT_URL https://github.com/cabasvert/cabasvert-
client/releases/download/v${CLIENT_VERSION}/${CLIENT_ARCHIVE}  
  
# Add Tini  
#ENV TINI_VERSION v0.16.1  
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
#RUN chmod +x /usr/bin/tini  
#ENTRYPOINT ["/usr/bin/tini", "--"]  
RUN mkdir -p /usr/src/app  
  
# Fetch application server release in /tmp  
ADD ${SERVER_URL} /tmp  
RUN cd /tmp \  
&& tar -xzf ${SERVER_ARCHIVE} \  
&& cp -r package/* /usr/src/app/ \  
&& rm -rf /tmp/package \  
&& cd /usr/src/app \  
&& npm install --production  
  
# Fetch application browser client release in /tmp  
ADD ${CLIENT_URL} /tmp  
RUN cd /tmp \  
&& tar -xzf ${CLIENT_ARCHIVE} \  
&& cp -r www/* /usr/src/app/public/ \  
&& rm -rf /tmp/www  
  
# Install application  
WORKDIR /usr/src/app  
RUN chown -R node:node /usr/src/app  
  
# Run application  
USER node  
ENV NODE_ENV production  
EXPOSE 8080  
CMD node dist/cli --config=${SERVER_CONFIG_FILE} \--generate-client-
config=${NODE_ENV}  

