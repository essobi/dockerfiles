# Base image:  
FROM alpine:3.7  
RUN apk add --no-cache curl bash  
  
ADD init.sh /tasks/init.sh  
  
WORKDIR /tasks  
  
CMD /tasks/init.sh  

