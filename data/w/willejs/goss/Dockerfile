FROM alpine:3.3  
  
RUN apk add --no-cache curl ca-certificates \  
&& curl -L https://github.com/aelsabbahy/goss/releases/download/v0.0.22/goss-
linux-amd64 -o /usr/local/bin/goss \  
&& chmod +x /usr/local/bin/goss \  
&& apk del ca-certificates  
  
ENTRYPOINT ["goss", "validate"]  

