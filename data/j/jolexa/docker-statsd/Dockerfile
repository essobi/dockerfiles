FROM mhart/alpine-node:base  
  
WORKDIR /src  
ADD . /src  
  
RUN apk update && \  
apk add ca-certificates && \  
update-ca-certificates && \  
apk add openssl && \  
wget http://github.com/etsy/statsd/archive/v0.8.0.tar.gz && \  
tar -xf v0.8.0.tar.gz  
  
EXPOSE 8125/udp  
EXPOSE 8125  
EXPOSE 8126  
CMD ["node", "statsd-0.8.0/stats.js", "config.js"]  
  

