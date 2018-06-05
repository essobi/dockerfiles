FROM alpine:3.5  
ENV HUGO_VERSION 0.30.1  
# Install HUGO  
RUN set -x && \  
apk add --update asciidoctor ca-certificates curl wget && \  
wget
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
&& \  
tar xzf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \  
rm -r hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \  
mv hugo /usr/bin/hugo && \  
apk del wget ca-certificates && \  
rm /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/hugo"]  

