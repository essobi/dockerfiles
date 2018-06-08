FROM alpine  
  
MAINTAINER Mei Akizuru <chimeaquas@hotmail.com>  
  
ENV HUGO_VERSION 0.16  
RUN apk add --update curl && \  
curl -L -o /tmp/hugo.tgz
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_linux-64bit.tgz
&& \  
tar xf /tmp/hugo.tgz -C /tmp && \  
mv /tmp/hugo /usr/local/bin/hugo && \  
rm -rf /tmp/*  
  
ENTRYPOINT ["hugo"]  

