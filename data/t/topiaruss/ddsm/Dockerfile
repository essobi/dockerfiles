FROM ubuntu:trusty  
  
MAINTAINER russf@topia.com  
  
RUN apt-get update -qy  
  
RUN apt-get install -qy git ruby g++ imagemagick  
  
COPY scripts/*.sh /  
  
CMD ["./go.sh"]  
  

