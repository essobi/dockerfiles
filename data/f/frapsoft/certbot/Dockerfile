FROM alpine  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
RUN apk update && \  
apk add --no-cache certbot && \  
rm -rf /var/cache/apk/*  
  
# RUN apk add --no-cache ca-certificates && apk add --no-cache openssl  
ENTRYPOINT ["certbot"]  
  
CMD ["--help"]  

