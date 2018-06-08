FROM nginx:1.13.10-alpine  
  
RUN apk add openssl --update && \  
rm -rf /var/cache/apk/* && \  
rm -rf /etc/nginx/*  
  
COPY run-proxy /bin/run-proxy  
  
ENTRYPOINT ["/bin/run-proxy"]  

