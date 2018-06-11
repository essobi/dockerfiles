FROM debian:8.5  
RUN apt-get update && \  
apt-get install -y wget && \  
apt-get clean  
  
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-
init_1.1.3_amd64.deb  
  
RUN dpkg -i dumb-init_*.deb  
  
ADD echo.sh /root/echo.sh  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
  
CMD ["/bin/bash", "/root/echo.sh"]  

