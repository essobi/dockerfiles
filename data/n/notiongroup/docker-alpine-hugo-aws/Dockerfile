FROM alpine:3.2  
MAINTAINER Chris Baker <cgbaker@cgbaker.net>  
  
ENV HUGO_VERSION 0.17  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux-64bit  
  
# Install AWS tools as well  
RUN mkdir -p /aws  
# Install pygments (for syntax highlighting) and bash  
RUN apk update && \  
apk add py-pygments && \  
apk add bash git && \  
apk -Uuv add groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm -rf /var/cache/apk/*  
  
# Download and Install hugo  
RUN mkdir /usr/local/hugo  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
/usr/local/hugo/  
RUN tar xzf /usr/local/hugo/${HUGO_BINARY}.tar.gz -C /usr/local/hugo \  
&& ln -s
/usr/local/hugo/hugo_${HUGO_VERSION}_linux_amd64/hugo_${HUGO_VERSION}_linux_amd64
/usr/local/bin/hugo \  
&& rm /usr/local/hugo/${HUGO_BINARY}.tar.gz  
  
EXPOSE 1313  
CMD hugo version  

