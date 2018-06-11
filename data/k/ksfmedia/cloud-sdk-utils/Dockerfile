FROM google/cloud-sdk:alpine  
  
# Add docker. It is in community repos, which of course are not default  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN apk update  
RUN apk add docker bash  

