FROM alpine:3.2  
RUN apk add -U gpgme  
RUN gpg || true  
  
ENTRYPOINT ["gpg"]  

