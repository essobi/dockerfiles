FROM alpine  
  
RUN mkdir /root/wkspace  
WORKDIR /root/wkspace  
  
RUN apk add --no-cache build-base go ruby python bash imagemagick  
  
COPY files/ /root  
  
CMD sh  

