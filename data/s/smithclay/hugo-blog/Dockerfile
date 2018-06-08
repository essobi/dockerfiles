FROM alpine:3.3  
MAINTAINER smithclay@gmail.com  
  
ENV HUGO_VERSION 0.15  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux_amd64  
  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
/usr/local/  
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/ \  
&& ln -s /usr/local/${HUGO_BINARY}/${HUGO_BINARY} /usr/local/bin/hugo \  
&& rm /usr/local/${HUGO_BINARY}.tar.gz  
  
# Create working directory  
RUN mkdir -p /etc/nginx/html  
RUN mkdir -p /usr/share/blog  
WORKDIR /usr/share/blog  
  
# For a data volume  
CMD true  

