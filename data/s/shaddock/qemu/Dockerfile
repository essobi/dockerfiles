FROM shaddock/seed:juno  
MAINTAINER Thibaut Lapierre <root@epheo.eu>  
  
#install nova  
RUN apt-get update  
RUN apt-get install -y nova-compute sysfsutils qemu libguestfs-tools nova-
network nova-api-metadata  
  
#Setup supervisord  
ADD supervisord.conf /etc/supervisord.conf  
  
VOLUME ["/var/log/nova"]  
  
ADD nova-start /usr/local/bin/  
ADD configparse.py /usr/local/bin/  
RUN chmod +x /usr/local/bin/nova-start  
RUN chmod +x /usr/local/bin/configparse.py  
  
EXPOSE 8775  
CMD ["nova-start"]  

