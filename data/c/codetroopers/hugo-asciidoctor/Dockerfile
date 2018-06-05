FROM rochdev/alpine-asciidoctor  
  
ENV HUGO_VERSION 0.15  
RUN apk add --update curl && \  
curl -L
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_linux_amd64.tar.gz
| tar xvz -C /tmp && \  
mv /tmp/hugo_${HUGO_VERSION}_linux_amd64/hugo_${HUGO_VERSION}_linux_amd64
/usr/local/bin/hugo && \  
rm -rf /tmp/hugo_${HUGO_VERSION}_linux_amd64/  
  
EXPOSE 1313  

