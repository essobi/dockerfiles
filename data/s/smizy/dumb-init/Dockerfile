FROM alpine:3.3  
MAINTAINER smizy  
  
ENV DUMB_INIT_VERSION 1.0.2  
  
RUN apk \--no-cache add \--virtual .builddeps \  
ca-certificates \  
gcc \  
musl-dev \  
&& wget -q -O - https://github.com/Yelp/dumb-
init/archive/v${DUMB_INIT_VERSION}.tar.gz \  
| tar -xzf - -C /tmp \  
&& gcc -std=gnu99 -s -Wall -Werror -O3 -o /sbin/dumb-init \  
/tmp/dumb-init-${DUMB_INIT_VERSION}/dumb-init.c \  
&& apk del .builddeps \  
&& rm -rf /tmp/dumb-init-${DUMB_INIT_VERSION}

