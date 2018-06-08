FROM frolvlad/alpine-glibc:alpine-3.4  
MAINTAINER euforia  
  
RUN apk add --update ca-certificates  
  
ADD ./nomad-0.5.5-dev.tgz /usr/bin/  
  
ENTRYPOINT ["/usr/bin/nomad"]  

