FROM alpine:3.6  
MAINTAINER Jordan Clark jordan.clark@esu10.org  
  
RUN apk add --no-cache curl bash openssl && \  
apk --no-cache --update upgrade && \  
curl --silent https://raw.githubusercontent.com/srvrco/getssl/master/getssl
--output /usr/local/bin/getssl && \  
chmod +x /usr/local/bin/getssl  
  
#COPY container-files /  
ENTRYPOINT ["/usr/local/bin/getssl"]  

