FROM alpine:edge  
COPY vendor/github.com/colstrom/package.sh/bin/* /usr/local/bin/  
RUN mkdir -p /usr/local/sbin \  
&& echo http://dl-cdn.alpinelinux.org/alpine/edge/main | tee
/etc/apk/repositories \  
&& echo @testing http://dl-cdn.alpinelinux.org/alpine/edge/testing | tee -a
/etc/apk/repositories \  
&& echo @community http://dl-cdn.alpinelinux.org/alpine/edge/community | tee
-a /etc/apk/repositories \  
&& apk add --update openssl \  
&& wget -q -O /usr/local/sbin/apk-install
https://raw.githubusercontent.com/gliderlabs/docker-
alpine/master/builder/scripts/apk-install \  
&& wget -q -O /usr/local/bin/owner
https://raw.githubusercontent.com/colstrom/owner/master/bin/owner \  
&& apk del openssl \  
&& chmod a+x /usr/local/sbin/apk-install /usr/local/bin/owner \  
&& rm -rf /var/cache/apk/*  

