FROM alpine:latest  
RUN apk add --no-cache openssl && apk add --no-cache --repository
http://nl.alpinelinux.org/alpine/edge/testing hitch && mkdir -p /etc/hitch  
COPY run.sh /run.sh  
ENTRYPOINT ["/run.sh"]  

