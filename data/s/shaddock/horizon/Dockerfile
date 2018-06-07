FROM shaddock/seed:latest  
MAINTAINER Thibaut Lapierre <root@epheo.eu>  
  
#install horizon  
RUN apt-get update  
RUN apt-get install -y openstack-dashboard apache2 libapache2-mod-wsgi
memcached python-memcache  
RUN apt-get remove -y --purge openstack-dashboard-ubuntu-theme  
  
#Setup supervisord  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
VOLUME ["/var/log/horizon"]  
  
ADD horizon-start /usr/local/bin/  
RUN chmod +x /usr/local/bin/horizon-start  
  
EXPOSE 80  
EXPOSE 11211  
CMD ["horizon-start"]  

