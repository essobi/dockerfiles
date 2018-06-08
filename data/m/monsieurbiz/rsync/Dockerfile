FROM alpine  
  
LABEL maintainer "Monsieur Biz <docker@monsieurbiz.com>"  
  
RUN apk update && \  
apk add openssh rsync  
  
ENTRYPOINT ["/usr/bin/rsync"]  

