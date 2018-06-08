FROM debian:jessie  
MAINTAINER François Billant <fbillant@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y \  
heirloom-mailx  
  
COPY smtp_monitor.sh /root/smtp_monitor.sh  
RUN chmod +x /root/smtp_monitor.sh  
  
CMD ["/root/smtp_monitor.sh"]  
  

