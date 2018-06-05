FROM alpine  
  
RUN apk add --no-cache aria2  
  
VOLUME /data  
  
EXPOSE 6800  
CMD ["aria2c", "--dir=/data", "--enable-rpc=true", "--rpc-listen-all=true", "
--rpc-allow-origin-all=true", "--continue=true", "--max-connection-per-
server=10", "--min-split-size=10M", "--split=10", "--file-
allocation=prealloc"]  
  

