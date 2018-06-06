FROM alpine:3.3  
RUN apk add --update --no-cache unbound bash  
  
COPY docker-entrypoint.sh /root/docker-entrypoint.sh  
COPY unbound.conf /etc/unbound/unbound.conf  
  
ENTRYPOINT [ "/root/docker-entrypoint.sh" ]  
  
CMD [ "unbound", "-d" ]

