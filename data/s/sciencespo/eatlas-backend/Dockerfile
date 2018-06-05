FROM node:carbon-alpine  
  
ENV NODE_ENV production  
  
ENV NODE_CONFIG_DIR /eatlas/config/  
  
COPY server/package.json server/yarn.lock /eatlas/server/  
COPY client/ /eatlas/client/  
  
RUN apk add --no-cache su-exec git  
  
RUN cd /eatlas/server && yarn install --frozen-lockfile --no-cache
--production \  
&& cd /eatlas/client && yarn install --frozen-lockfile --no-cache
--production=false \  
&& rm -fr /usr/local/share/.cache/*  
  
COPY config/ /eatlas/config/  
COPY server/ /eatlas/server/  
  
RUN mkdir -p /eatlas/data/uploads && chown -R node:node /eatlas/data/uploads  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
WORKDIR /eatlas/server/  
  
EXPOSE 4000  
VOLUME /eatlas/client/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

