FROM alpine  
MAINTAINER dentych  
  
RUN echo "@testing http://dl-3.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk update && \  
apk add whois@testing  
  
ENTRYPOINT ["whois"]  
CMD ["--help"]  

