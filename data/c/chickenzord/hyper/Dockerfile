FROM alpine:3.4  
MAINTAINER Akhyar Amarullah "akhyrul@gmail.com"  
# system dependencies  
RUN apk update && apk add wget tar openssl ca-certificates \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
# workaround, because hyper-cli needs glibc that's not available on alpine by
default  
# https://github.com/sgerrand/alpine-pkg-glibc  
ARG GLIBC_VERSION=2.23-r3  
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget -q -O /tmp/glibc.apk https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk \  
&& apk add /tmp/glibc.apk && rm /tmp/glibc.apk  
  
# install hyper  
RUN wget -q -O /tmp/hyper.tar.gz https://hyper-install.s3.amazonaws.com/hyper-
linux-x86_64.tar.gz \  
&& tar -xzf /tmp/hyper.tar.gz -C /usr/bin && chmod +x /usr/bin/hyper \  
&& rm /tmp/hyper.tar.gz  
  
VOLUME /root/.hyper/config.json:ro  
CMD hyper  

