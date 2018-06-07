FROM redis:alpine  
  
# Install bash python curl  
RUN apk add --no-cache bash  
  
COPY redis-sentinel-entrypoint.sh /redis-sentinel-entrypoint.sh  
COPY sentinel-configurator.sh /sentinel-configurator.sh  
  
ENV QUORUM 1  
ENV DOWN_AFTER_MS 30000  
ENV FAILOVER_TIMEOUT 60000  
ENV PARALLEL_SYNCS 1  
ENTRYPOINT [ "/redis-sentinel-entrypoint.sh" ]  

