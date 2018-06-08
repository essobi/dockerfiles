FROM alpine:latest  
RUN apk add --no-cache --repository http://nl.alpinelinux.org/alpine/edge/main
varnish  
COPY ./vmods/install /  
COPY run.sh /  
ENTRYPOINT ["/run.sh"]  

