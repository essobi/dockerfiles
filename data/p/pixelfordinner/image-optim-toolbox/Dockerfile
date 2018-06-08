FROM alpine:3.5  
MAINTAINER Karl Fathi <karl@pixelfordinner.com>  
  
ENV LANG C.UTF-8  
RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
RUN apk add --no-cache \  
su-exec \  
jpegoptim@testing \  
optipng \  
gifsicle  
  
ADD ./data/bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
  
ENTRYPOINT ["entrypoint"]  

