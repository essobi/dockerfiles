FROM stellar/base:latest  
  
MAINTAINER Mat Schaffer <mat@stellar.org>  
  
ENV ATLAS_VERSION 1.4.5  
EXPOSE 7101  
ADD install /  
RUN /install  
  
ADD /conf/* /etc/atlas/  
ADD start /  
  
CMD ["/start"]  

