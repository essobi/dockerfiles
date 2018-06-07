FROM python:3.4-slim  
  
ENV DEVPI_VERSION=4.2.1  
ENV DEVPI_SERVERDIR=/data/server DEVPI_CLIENTDIR=/data/client
DEVPI_SERVERPORT=3140  
RUN apt-get update && \  
apt-get install -y --no-install-recommends supervisor unzip nginx wget patch
&& \  
# apt-get install -y --no-install-recommends python-pip python-setuptools
python-wheel && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD install /tmp  
  
RUN /tmp/install_devpi.sh && /tmp/install_nginx.sh &&
/tmp/install_devpi_client.sh && \  
rm -rv /tmp/* && rm -rv ~/.cache/pip  
  
ADD run.sh initialize.sh /  
  
ADD nginx/nginx-devpi.conf /etc/nginx/sites-enabled/default  
  
ADD *.conf /etc/supervisor/conf.d/  
  
VOLUME /data  
  
EXPOSE 80  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]  

