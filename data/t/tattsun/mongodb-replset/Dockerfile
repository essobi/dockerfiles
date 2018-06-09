FROM dockerfile/mongodb:latest  
  
MAINTAINER tattsun <t.t.mc1192.sf@gmail.com>  
  
RUN apt-get update && \  
apt-get -y install git python-setuptools && \  
easy_install supervisor && \  
apt-get clean && \  
mkdir -p /data/node1 && \  
mkdir -p /data/node2 && \  
mkdir -p /data/node3 && \  
echo_supervisord_conf > /etc/supervisord.conf && \  
echo '[include]' >> /etc/supervisord.conf && \  
echo 'files = supervisord/conf/*.conf' >> /etc/supervisord.conf && \  
mkdir -p /etc/supervisord/conf/  
  
ADD ./supervisor.conf /etc/supervisord/conf/service.conf  
ADD ./config /root/config  
ADD ./run /root/run  
  
EXPOSE 27017 27018 27019  
CMD ["/root/run"]  

