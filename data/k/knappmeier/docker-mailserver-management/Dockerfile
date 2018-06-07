FROM node:8  
# Add Tini (https://github.com/krallin/tini#using-tini)  
ENV TINI_VERSION v0.16.1  
ADD "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini"
/bin/tini  
ADD "https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64"
/bin/gosu  
RUN chmod a+x /bin/tini /bin/gosu  
  
VOLUME /tmp/docker-mailserver  
WORKDIR /app  
ADD package.json /app  
RUN npm install --production  
  
ADD . /app  
  
RUN chmod a+x /app/entrypoint.sh  
  
ENTRYPOINT ["/app/entrypoint.sh"]  
CMD ["npm", "start"]

