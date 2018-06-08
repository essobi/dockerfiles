FROM shaddock/seed:latest  
MAINTAINER Thibaut Lapierre <root@epheo.eu>  
  
RUN pip uninstall -y pbr  
RUN apt-get update &&\  
apt-get install -y neutron-server neutron-plugin-ml2 neutron-linuxbridge-agent
\  
neutron-l3-agent neutron-dhcp-agent neutron-metadata-agent  
  
ADD supervisord.conf /etc/supervisord.conf  
  
VOLUME ["/var/log/neutron"]  
  
ADD neutron-start /usr/local/bin/  
ADD configparse.py /usr/local/bin/  
RUN chmod +x /usr/local/bin/neutron-start  
RUN chmod +x /usr/local/bin/configparse.py  
  
<<<<<<< HEAD  
EXPOSE 9774  
EXPOSE 8775  
=======  
>>>>>>> mitaka  
EXPOSE 9696  
CMD ["neutron-start"]  

