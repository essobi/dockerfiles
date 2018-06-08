FROM ubuntu:14.04  
ENV NAME Genesis  
RUN apt-get update  
RUN apt-get install -y vim  
  
ADD src/ /opt/app/  
  
WORKDIR /opt/app  
  
CMD echo $NAME  
  

