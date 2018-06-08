FROM shaddock/seed:latest  
MAINTAINER Thibaut Lapierre <root@epheo.eu>  
  
#install glance  
RUN apt-get -y update  
RUN pip uninstall -y pbr  
RUN apt-get install -y --force-yes glance  
  
ADD supervisord.conf /etc/supervisord.conf  
  
VOLUME ["/var/log/glance", "/var/lib/glance/images"]  
  
ADD glance-start /usr/local/bin/  
ADD configparse.py /usr/local/bin/  
RUN chmod +x /usr/local/bin/glance-start  
RUN chmod +x /usr/local/bin/configparse.py  
  
EXPOSE 9292  
EXPOSE 9191  
CMD ["glance-start"]  

