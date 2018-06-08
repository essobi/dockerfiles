FROM alpine:3.3  
  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
RUN apk add --update linux-headers gcc openssl-dev musl-dev libffi-dev python-
dev py-pip \  
&& pip install --no-cache-dir letsencrypt \  
&& apk info | grep dev | xargs apk del \  
&& apk del scanelf gcc musl-utils libc-utils pkgconf pkgconfig linux-headers \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 443  

