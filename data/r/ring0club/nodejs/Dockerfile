FROM alpine:3.7  
RUN apk upgrade --no-cache  
RUN apk add libuv=1.20.2-r0 \  
http-parser=2.8.1-r0 \  
\--repository https://nl.alpinelinux.org/alpine/edge/main \  
\--no-cache  
RUN apk add nodejs-current=9.11.1-r2 \  
\--repository https://nl.alpinelinux.org/alpine/edge/community \  
\--no-cache  
ENTRYPOINT ["/bin/sh"]  

