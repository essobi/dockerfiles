FROM alpine:edge  
  
# CLI  
ENV VERSION 1.5.1-r0  
  
RUN apk --update add yarn=$VERSION && rm -rf /var/cache/apk/*  
  
ENTRYPOINT [ "yarn" ]  

