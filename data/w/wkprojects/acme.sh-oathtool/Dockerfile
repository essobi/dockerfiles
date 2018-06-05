FROM neilpang/acme.sh  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& apk add --no-cache oath-toolkit-oathtool \  
&& rm -rf /var/cache/apk/*  

