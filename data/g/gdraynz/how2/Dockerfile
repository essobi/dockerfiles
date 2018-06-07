FROM alpine:3.7  
RUN apk add --update nodejs && \  
npm install -g how-2 && \  
npm cache clean --force && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["how2"]  

