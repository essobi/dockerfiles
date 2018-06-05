FROM node:6  
LABEL maintainer docker@katagena.com  
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-gandi-mail"  
LABEL version="latest"  
  
ENV GANDI_API_KEY=TATAYOYO  
ENV GANDI_DOMAIN=example.com  
  
WORKDIR /usr/src/app  
RUN npm install xmlrpc csv-streamify sleep  
  
COPY index.js /usr/src/app/index.js  
  
ENTRYPOINT node index.js  

