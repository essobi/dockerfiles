FROM alpine:latest  
  
RUN apk add --no-cache squid gawk curl  
  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3128-3129 3130/udp 3401/udp  
#USER squid  

