FROM alpine:3.3  
  
MAINTAINER shufo  
  
ENV PHANTOMJS_VERSION 1.9.8  
  
RUN apk add --update \--no-cache curl && \  
curl -Ls
"https://github.com/dustinblackman/phantomized/releases/download/2.1.1/dockerized-
phantomjs.tar.gz" | tar xz -C / && \  
curl -k -Ls
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2
| tar -jxvf - -C / && \  
cp phantomjs-${PHANTOMJS_VERSION}-linux-x86_64/bin/phantomjs
/usr/local/bin/phantomjs && \  
rm -fR phantomjs-${PHANTOMJS_VERSION}-linux-x86_64 && \  
apk del curl  
  
ENTRYPOINT ["/usr/local/bin/phantomjs"]  

