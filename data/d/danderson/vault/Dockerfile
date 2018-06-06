FROM alpine:edge  
RUN \  
echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing"
>>/etc/apk/repositories &&\  
apk -U add vault@testing &&\  
rm -rf /var/cache/apk/*  
ENTRYPOINT /usr/sbin/vault  

