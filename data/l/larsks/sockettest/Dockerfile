FROM alpine  
  
RUN apk update  
RUN apk add socat  
  
COPY sockettest.sh /sockettest.sh  
CMD ["/sockettest.sh"]  

