FROM alpine:3.6  
ADD VERSION .  
  
ENV HUGO_VERSION 0.32.3  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux-64bit  
  
# Install pygments (for syntax highlighting)  
RUN apk update && apk add py-pygments && apk add git && apk add bash && rm -rf
/var/cache/apk/*  
  
# Download and Install hugo  
ADD
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
/usr/local/  
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/bin/ \  
&& rm /usr/local/${HUGO_BINARY}.tar.gz  

