FROM alpine:latest  
  
LABEL maintainer="support@opensvc.com"  
  
RUN apk --update add --no-cache python3 py3-requests  
  
COPY src /usr/share/igw_gobetween  
  
ENTRYPOINT ["/usr/share/igw_gobetween/gobtw_janitor"]  
  

