FROM alpine:latest  
  
RUN apk add --update nodejs bash &&\  
rm -rf /var/cache/apk/* &&\  
npm install -g npm &&\  
npm install -g forever &&\  
rm -rf ~/.npm/* &&\  
rm -rf /tmp/*  

