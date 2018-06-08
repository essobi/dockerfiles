FROM alpine:3.6  
MAINTAINER Lorelei Aurora <iam@l5i.me>  
  
ENTRYPOINT /entrypoint.sh  
  
RUN apk add --no-cache \  
ca-certificates \  
openssl  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["openssl"]

