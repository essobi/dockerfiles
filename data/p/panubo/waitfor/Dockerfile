FROM alpine:latest  
  
MAINTAINER Andrew Cutler <andrew@panubo.com>  
  
RUN apk add --update bash && \  
rm -rf /var/cache/apk/*  
  
COPY entry.sh /  
  
ENTRYPOINT ["/entry.sh"]  

