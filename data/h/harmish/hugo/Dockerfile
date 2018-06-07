FROM alpine  
  
# download latest hugo release  
RUN apk add --update curl openssl && \  
HUGO_VERSION=$(curl -L -s -H 'Accept: application/json'
https://github.com//gohugoio/hugo/releases/latest | sed -e
's/.*"tag_name":"v\\([^"]*\\)".*/\1/') && \  
wget -O /tmp/hugo.tar.gz
https://github.com//gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
&& \  
tar xz -C /tmp -f /tmp/hugo.tar.gz && \  
mv /tmp/hugo /usr/bin/hugo && \  
rm -rf /tmp/*  
  
EXPOSE 1313  

