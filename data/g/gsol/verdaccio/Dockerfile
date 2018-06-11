FROM node:6.11.0-alpine  
MAINTAINER Global Solutions co., ltd.  
LABEL version="2.2.0"  
  
WORKDIR "/home/node/verdaccio"  
ADD package.json config.yaml /home/node/verdaccio/  
  
RUN npm install --production && \  
mkdir storage local_storage && \  
npm cache -f clean && \  
chown node:node . -R  
  
USER node  
VOLUME ["/home/node/verdaccio/storage", "/home/node/verdaccio/local_storage"]  
EXPOSE 4873  
ENTRYPOINT ["npm"]  
CMD ["start", "--", "--config", "/home/node/verdaccio/config.yaml"]  

