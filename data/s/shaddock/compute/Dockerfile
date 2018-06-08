FROM shaddock/seed:latest  
MAINTAINER Thibaut Lapierre <root@epheo.eu>  
  
#install nova  
RUN apt-get update  
RUN apt-get install -y --force-yes nova-compute sysfsutils qemu \  
libguestfs-tools nova-network \  
nova-api-metadata  
  
RUN git clone https://github.com/lxc/nova-compute-lxd &&\  
cd nova-compute-lxd && python setup.py install  
  
#Setup supervisord  
ADD supervisord.conf /etc/supervisord.conf  
  
VOLUME ["/var/log/nova"]  
  
ADD nova-start /usr/local/bin/  
ADD configparse.py /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/configparse.py &&\  
chmod +x /usr/local/bin/nova-start  
  
EXPOSE 8775  
CMD ["nova-start"]  

