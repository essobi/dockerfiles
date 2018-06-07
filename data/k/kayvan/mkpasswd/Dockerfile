# Simple alpine linux python based mkpasswd  
#  
FROM alpine:3.3  
  
MAINTAINER Kayvan Sylvan <kayvansylvan@gmail.com>  
  
RUN apk update && apk upgrade  
  
RUN apk add --no-cache py-pip  
RUN pip install --upgrade pip  
RUN pip install passlib  
  
RUN rm -rf /usr/share/man /tmp/* /var/cache/apk/* /root/.npm \  
/root/.node-gyp /root/.gnupg /usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html  
  
COPY mkpasswd /usr/bin/  
  
ENTRYPOINT [ "/usr/bin/mkpasswd" ]  

