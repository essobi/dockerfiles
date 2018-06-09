FROM alpine:3.1  
MAINTAINER thinkeride <thinkeridea@sina.com>  
  
ENV HUGO_VERSION 0.25.1  
# Install HUGO  
RUN set -x \  
&& apk add --update wget ca-certificates \  
&& wget
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
\  
&& tar xzf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz \  
&& mv hugo /usr/bin/hugo \  
&& apk del wget ca-certificates \  
&& rm -rf /var/cache/apk/* hugo hugo_${HUGO_VERSION}_Linux-64bit.tar.gz  
  
ENTRYPOINT ["/usr/bin/hugo"]  

