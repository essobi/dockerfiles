FROM nginx  
MAINTAINER Pablo Moncada Isla <pmoncadaisla@gmail.com>  
  
  
RUN \  
apt-get update && \  
apt-get install -y wget  
  
ADD run.sh /run.sh  
  
ENV URL_FILE http://google.com  
  
CMD ["/run.sh"]  
  

