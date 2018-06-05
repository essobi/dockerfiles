FROM alpine:3.5  
ENV INTERFACES=  
  
RUN apk add --update --no-cache dhcp  
  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME /var/lib/dhcp  
  
ENTRYPOINT ["/entrypoint.sh"]  

