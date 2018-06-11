FROM gliderlabs/alpine:3.2  
  
RUN apk-install openssl \  
&& wget -qO- https://github.com/Rushmorefm/alpine-
packages/releases/download/v0.2/testing.tar.xz | tar xJ \  
&& apk --allow-untrusted -X /testing -X
http://dl-2.alpinelinux.org/alpine/edge/testing -U add python35 \  
&& rm -rf /testing /var/cache/apk/* \  
&& pip3 install virtualenv  

