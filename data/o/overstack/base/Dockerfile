FROM alpine:3.2  
MAINTAINER SHS <shs@overstack.ru>  
  
RUN apk update && apk upgrade \  
apk add curl bash jq tar gzip ca-certificates lsof && \  
rm -rf /var/cache/apk/* /usr/local/src/*  
  
CMD ["bash"]  

