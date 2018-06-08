FROM ukti/base-ubuntu  
  
RUN apt-get update -y && \  
apt-get install -y nginx dnsmasq  
  
ADD /root /  
RUN chmod a+x /etc/services/*/run  
  
EXPOSE 80 443  

