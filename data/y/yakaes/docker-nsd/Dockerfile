FROM alpine  
  
RUN \  
apk --no-cache add nsd openssl  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["server"]  
  

