FROM alpine:3.1  
ENV HUGO_VERSION 0.14  
# Install HUGO  
RUN set -x && \  
apk add --update wget ca-certificates && \  
wget
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_linux_amd64.tar.gz
&& \  
tar xzf hugo_${HUGO_VERSION}_linux_amd64.tar.gz && \  
rm -r hugo_${HUGO_VERSION}_linux_amd64.tar.gz && \  
mv hugo_${HUGO_VERSION}_linux_amd64/hugo_${HUGO_VERSION}_linux_amd64
/usr/bin/hugo && \  
rm -r hugo_${HUGO_VERSION}_linux_amd64 && \  
apk del wget ca-certificates && \  
rm /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/hugo"]  

