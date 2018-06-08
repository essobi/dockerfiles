FROM alpine:3.7  
  
LABEL net.quadric.vendor="Quadric ApS" maintainer="Ahmed Magdy
<ahmed.magdy@quadric.net>"  
RUN apk update && \  
apk add --update \--no-cache ca-certificates wget openssl curl && \  
update-ca-certificates && \  
rm -rf /var/cache/apk/*  
  
# ENTRYPOINT ["/usr/bin/curl"]  

