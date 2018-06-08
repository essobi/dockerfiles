FROM nginx  
  
MAINTAINER Marcelo Teixeira Monteiro  
  
ADD start.sh /usr/bin/  
  
RUN apt-get update && \  
apt-get -y install git && \  
chmod +x /usr/bin/start.sh  
  
EXPOSE 80  
CMD ["/usr/bin/start.sh"]  
  

