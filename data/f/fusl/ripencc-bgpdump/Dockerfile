FROM alpine:edge  
LABEL maintainer="Katie Holly <holly@fuslvz.ws>"  
ENV BGPDUMP_VERSION 1.5.00.00  
ADD tmp /tmp/build-tmp  
RUN apk upgrade --no-cache \  
&& apk add --no-cache curl autoconf gcc libc-dev zlib-dev bzip2-dev make \  
&& curl -s -o -
https://bitbucket.org/ripencc/bgpdump/get/${BGPDUMP_VERSION}.tar.gz | tar -xzC
/tmp/build-tmp --strip-components=1 \  
&& cd /tmp/build-tmp \  
&& ./bootstrap.sh \  
&& patch < /tmp/build-tmp/patch \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /tmp/build-tmp  
ENTRYPOINT ["bgpdump"]  

