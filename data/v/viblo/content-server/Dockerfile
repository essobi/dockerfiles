FROM node:8-alpine  
  
RUN apk update && apk add --no-cache git tini  
  
RUN which node  
  
ENV NODE_ENV=production  
ENV PORT=3000  
ENV API_URL=https://api.viblo.asia  
ENV APP_URL=https://viblo.asia  
  
ENV TINI_VERSION v0.16.1  
COPY . /srv  
WORKDIR /srv  
  
RUN yarn install  
RUN apk del git  
  
EXPOSE 3000  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/usr/local/bin/node", "/srv/src/server.js"]  

