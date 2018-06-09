FROM node:alpine  
  
MAINTAINER Andrew Cutler <andrew@panubo.com>  
  
RUN apk add --update bash findutils gzip curl && \  
rm -rf /var/cache/apk/*  
  
RUN npm install -g couchdb-dump  
  
COPY commands /commands  
  
ENTRYPOINT ["/commands/entry.sh"]  
  
CMD ["default"]  

