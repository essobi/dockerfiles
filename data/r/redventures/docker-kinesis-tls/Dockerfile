FROM alpine:3.3  
COPY start-all.sh kinesalite.* kinesalite-nginx.conf /  
  
RUN apk add --no-cache python make g++ nodejs nginx && \  
npm install -g kinesalite && \  
apk del python make g++ && \  
rm -rf /tmp/* /var/cache/apk/* && \  
chmod 755 /start-all.sh  
  
EXPOSE 80 443  
ENTRYPOINT ["/start-all.sh"]  

