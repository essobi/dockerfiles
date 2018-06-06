FROM alpine:3.5  
MAINTAINER Andrew Cutler <andrew@panubo.com>  
  
RUN apk update && \  
apk add bash stunnel rsync && \  
rm -rf /var/cache/apk/*  
  
COPY rsync*.sh /usr/local/bin/  
  
COPY entry.sh /entry.sh  
  
ENTRYPOINT ["/entry.sh"]  

