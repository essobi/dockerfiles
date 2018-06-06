FROM alpine:latest  
  
RUN \  
apk add --update curl && \  
rm -rf /var/cache/apk/*  
  
ADD entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["curl"]  

