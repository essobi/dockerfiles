FROM alpine:3.5  
MAINTAINER Peter Dave Hello <hsu@peterdavehello.org>  
ADD cdnjs.fetch.sh /bin/  
ADD ColorEchoForShell/dist/ColorEcho.sh /  
RUN apk -U upgrade && \  
apk -v add git openssl && \  
rm -rf /var/cache/apk/*  
ENTRYPOINT /bin/cdnjs.fetch.sh  

