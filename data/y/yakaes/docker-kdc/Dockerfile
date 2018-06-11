FROM alpine  
  
RUN \  
apk --no-cache add krb5 krb5-server  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["server"]  
  

