FROM alpine:3.5  
MAINTAINER Karl Fathi <karl@pixelfordinner.com>  
  
ENV LANG C.UTF-8  
RUN addgroup -S duplicity && \  
mkdir -p /mnt/app && \  
adduser -D -S -u 1896 -h /mnt/app -s /sbin/nologin -G duplicity duplicity  
  
RUN apk add --no-cache \  
su-exec \  
duplicity \  
openssh \  
openssl \  
py-crypto \  
py-pip \  
rsync  
  
RUN pip install --upgrade pip  
RUN pip install pydrive  
  
RUN apk del --purge py-pip  
  
ADD ./data/bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
  
ENV HOME=/mnt/app  
  
ENTRYPOINT ["entrypoint"]  

