FROM debian:latest  
  
MAINTAINER benesis002@outlook.com  
  
RUN apt-get update && apt-get install -y wget  
RUN wget http://pqsoftware.eaton.com/install/linux/ipp/ipp-
linux_1.53.150-1_amd64.deb  
#RUN dpkg -i ipp-linux_1.53.150-1_amd64.deb  
ADD start.sh /root/start.sh  
RUN chmod +x /root/start.sh  
  
CMD ["/root/start.sh"]  
  
EXPOSE 4679  
HEALTHCHECK \--interval=5m --timeout=3s \  
CMD curl -f http://localhost:4679 || exit 1  

