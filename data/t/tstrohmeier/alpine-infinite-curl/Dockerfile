FROM alpine:3.7  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
RUN apk add --no-cache curl bash && \  
chmod +x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

