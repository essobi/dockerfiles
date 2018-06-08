FROM alpine:3.3  
RUN apk add --update socat && \  
rm -rf /var/cache/apk/*  
  
USER nobody  
ENTRYPOINT ["/usr/bin/socat"]  

