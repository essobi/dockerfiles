FROM gliderlabs/alpine:latest  
EXPOSE 80  
RUN apk add --no-cache lighttpd  
  
ADD ["lighttpd.conf", "mime-types.conf", "/etc/lighttpd/"]  
  
ENTRYPOINT ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

