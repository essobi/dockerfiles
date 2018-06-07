FROM alpine:edge  
MAINTAINER Christian Gatzlaff <cgatzlaff@gmail.com>  
  
RUN apk add --no-cache awake py-awake --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted  
  
# env variable  
ENV mac 11:11:11:11:11:11  
# start servers  
CMD awake ${mac}  

