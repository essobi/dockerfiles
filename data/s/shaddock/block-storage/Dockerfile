FROM shaddock/seed:latest  
MAINTAINER Thibaut Lapierre <root@epheo.eu>  
  
#install cinder  
RUN apt-get -y update  
RUN apt-get install -y --force-yes cinder-volume python-mysqldb lvm2  
  
ADD supervisord.conf /etc/supervisord.conf  
  
VOLUME ["/var/log/cinder"]  
VOLUME ["/var/lib/cindervols"]  
  
ADD cinder-start /usr/local/bin/  
ADD configparse.py /usr/local/bin/  
RUN chmod +x /usr/local/bin/cinder-start  
RUN chmod +x /usr/local/bin/configparse.py  
  
EXPOSE 3260  
CMD ["cinder-start"]  

