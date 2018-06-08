FROM ubuntu:14.04  
# make sure apt is up to date  
RUN apt-get update  
  
# install nodejs and npm  
RUN apt-get install -y nodejs npm git git-core  
  
RUN mkdir -p /var/www  
  
ADD start.sh /var/www/  
  
RUN chmod +x /var/www/start.sh  
  
EXPOSE 5000  
CMD sh /var/www/start.sh  

