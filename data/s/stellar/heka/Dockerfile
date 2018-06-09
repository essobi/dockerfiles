FROM stellar/base:latest  
  
MAINTAINER Mat Schaffer <mat@stellar.org>  
  
ENV HEKAD_VERSION 0.9.2  
ADD install /  
RUN /install  
  
ADD start /  
  
CMD ["/start"]  

