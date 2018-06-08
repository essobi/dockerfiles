FROM busybox  
  
VOLUME /secrets  
  
ADD copy.sh /copy.sh  
  
RUN mkdir -p /saved-secrets/  
  
CMD sh /copy.sh  

