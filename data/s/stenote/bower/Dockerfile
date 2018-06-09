FROM alpine:3.2  
RUN apk update && \  
apk add nodejs git && \  
rm -rf /var/cache/apk/*  
  
RUN npm install -g bower  
  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["bower", "--allow-root"]  

