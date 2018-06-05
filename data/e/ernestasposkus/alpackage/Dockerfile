FROM alpine:3.5  
ENV PACKAGES "openssl ca-certificates"  
RUN apk add --update openssl ca-certificates $PACKAGES && rm -rf
/var/cache/apk/*  

