FROM alpine  
  
RUN \  
apk --no-cache add nginx  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["server"]  
  

