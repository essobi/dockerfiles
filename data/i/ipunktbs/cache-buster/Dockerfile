FROM alpine:3.3  
COPY entrypoint.sh /usr/local/bin/  
RUN apk add --no-cache curl bash  
ENTRYPOINT ["/bin/bash", "/usr/local/bin/entrypoint.sh"]  

