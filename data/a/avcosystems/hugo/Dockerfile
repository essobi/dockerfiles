FROM alpine:latest  
  
ADD
https://github.com/gohugoio/hugo/releases/download/v0.38/hugo_0.38_Linux-64bit.tar.gz
/tmp  
RUN tar -xf /tmp/hugo_0.38_Linux-64bit.tar.gz -C /tmp \  
&& mv /tmp/hugo /usr/local/bin/hugo \  
&& rm -rf /tmp/*  
  
RUN apk add --update --no-cache git ca-certificates  
  
EXPOSE 1313/tcp  
  

