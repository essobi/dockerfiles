FROM alpine:latest  
  
LABEL maintainer="kr3ssh@pm.me"  
  
RUN apk add squid --no-cache  
  
RUN rm -rf /var/cache/apk/*  
  
ADD squid.conf /etc/squid/squid.conf  
ADD docker_entrypoint.sh /docker_entrypoint.sh  
  
EXPOSE 3128  
ENTRYPOINT ["/docker_entrypoint.sh"]  
  
CMD ["/usr/sbin/squid", "-N"]  

