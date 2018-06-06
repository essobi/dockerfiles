FROM ubuntu:14.04  
MAINTAINER Lukas Hetzenecker  
  
RUN apt-get update  
RUN apt-get install -yq postgresql-client  
  
# Add startup script  
ADD createdb /createdb  
  
CMD ["/createdb"]  
  

