FROM alpine:3.3  
RUN apk update && apk add nodejs && rm -rf /var/cache/apk/*  
RUN npm install -g typescript@1.8.2  
  
VOLUME "/app"  
  
WORKDIR "/app"  
  
CMD ["tsc"]  

