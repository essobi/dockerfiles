# Pull ubuntu base image.  
FROM ubuntu:14.04.4  
ENV VTUN_PASSWORD DONT_BE_DUPE_CHANGE_ME  
  
#Install packages on ubuntu base image  
RUN apt-get update && \  
apt-get install -y vtun && \  
apt-get install -y isc-dhcp-server && \  
apt-get install -y bridge-utils  
  
#Configure vtun and dhcp  
ADD config/vtund.conf /etc/vtund.conf  
ADD config/vtun /etc/default/vtun  
ADD init/vtun /etc/init.d/vtun  
RUN chmod +x /etc/init.d/vtun  
  
ADD config/isc-dhcp-server /etc/default/isc-dhcp-server  
ADD config/dhcpd.conf /etc/dhcp/dhcpd.conf  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  

