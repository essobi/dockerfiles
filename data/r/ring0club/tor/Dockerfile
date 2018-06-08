FROM alpine:3.7  
RUN apk upgrade --no-cache  
RUN apk add libressl2.7-libssl \  
libressl2.7-libcrypto \  
\--repository https://nl.alpinelinux.org/alpine/edge/main \  
\--no-cache  
RUN apk add tor=0.3.3.6-r0 \  
\--repository https://nl.alpinelinux.org/alpine/edge/community \  
\--no-cache  
#VOLUME /etc/tor  
USER tor  
ENTRYPOINT ["tor"]  

