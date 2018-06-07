FROM consul:0.7.5  
RUN \  
apk add --no-cache \  
drill  
  
COPY pre-entrypoint.sh /bin/pre-entrypoint.sh  
  
ENV DC=  
ENV DCS=  
ENV CONSUL_WEAVE_JOIN=  
ENV CONSUL_WEAVE_JOIN_WAN=  
ENV CONSUL_WEAVE_IP=  
  
ENTRYPOINT ["/bin/pre-entrypoint.sh"]  

