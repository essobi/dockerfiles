FROM alpine:3.6  
MAINTAINER Jordan Clark jordan.clark@esu10.org  
  
RUN apk add \--no-cache openssl && \  
apk --no-cache --update upgrade  
  
COPY container-files /  
  
ENTRYPOINT ["/gencert.sh"]  

