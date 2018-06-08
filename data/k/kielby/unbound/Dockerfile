FROM alpine:3.4  
RUN apk --no-cache add unbound  
  
EXPOSE 53/tcp 53/udp  
VOLUME /etc/unbound  
  
ENTRYPOINT ["unbound", "-d"]  

