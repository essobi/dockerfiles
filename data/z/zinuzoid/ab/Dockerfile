FROM alpine:edge  
MAINTAINER Jetsada Machom <jim@imjim.im>  
  
RUN apk --no-cache add \  
apache2-utils && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["ab"]  
  

