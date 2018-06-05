FROM node:7.10-alpine  
  
RUN apk add --no-cache tini && \  
apk add --no-cache sox && \  
rm -rf /var/cache/apk/*  
  
ADD server.js package.json config.json /  
ADD src/ src/  
  
RUN npm install  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["node", "server.js"]

