FROM upclose/python3  
  
RUN apk-install ffmpeg  
  
RUN apk-install openssl \  
&& wget -qO- https://github.com/Rushmorefm/alpine-
packages/releases/download/v0.4/testing.tar.xz | tar xJ \  
&& apk --allow-untrusted -X /testing -X
http://dl-2.alpinelinux.org/alpine/edge/testing -U add giflossy \  
&& rm -rf /testing /var/cache/apk/*  

