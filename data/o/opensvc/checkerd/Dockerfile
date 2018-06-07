FROM alpine:latest  
  
LABEL maintainer="support@opensvc.com"  
  
RUN apk --update add --no-cache python3 py3-requests fping  
  
COPY src /usr/share/checkerd  
  
ENTRYPOINT ["/usr/share/checkerd/checkerd.py"]  

