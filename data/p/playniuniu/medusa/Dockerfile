FROM alpine as builder  
LABEL maintainer="playniuniu@gmail.com"  
  
ENV MEDUSA_URL "http://foofus.net/goons/jmk/tools/medusa-2.2.tar.gz"  
RUN apk add --update curl openssl-dev libssh2-dev alpine-sdk  
RUN curl ${MEDUSA_URL} -o /tmp/medusa.tar.gz  
RUN tar -xzvf /tmp/medusa.tar.gz -C /tmp/  
RUN mkdir -p /opt/medusa  
RUN cd /tmp/medusa-2.2/ \  
&& ./configure --prefix=/opt/medusa --enable-module-ssh=yes \  
&& make \  
&& make install  
  
FROM alpine  
  
RUN apk add --no-cache --update libssh2 openssl  
COPY \--from=builder /opt/medusa /opt/medusa  
WORKDIR /opt/medusa/bin  
CMD ["./medusa"]  

