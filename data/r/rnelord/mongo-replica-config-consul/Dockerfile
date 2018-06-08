FROM mongo:3  
RUN apt-get update -qq && \  
apt-get install -y --no-install-recommends \  
dnsutils  
  
ENV NEXTRUN_WAIT_TIME 3  
ENV CONSUL_SERVICE_NAME mongo  
  
COPY bin/rs-config.sh /rs-config.sh  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh /rs-config.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

