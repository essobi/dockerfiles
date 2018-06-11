FROM alpine:3.5  
RUN apk --no-cache add openssh  
  
VOLUME /ssh  
  
EXPOSE 22  
ADD start.sh /start.sh  
RUN chmod u+x /start.sh  
CMD /start.sh  

