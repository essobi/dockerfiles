FROM nfqsolutions/miniconda3  
  
MAINTAINER solutions@nfq.com  
  
  
RUN apt-get update && \  
apt-get install -y supervisor gcc mysql-client mysql-server default-
libmysqlclient-dev librdkafka-dev && \  
pip install confluent-kafka  
  
# Variables de entorno  
ENV RPM_PATH=/solutions/app/rpm \  
PIP_PATH=/solutions/app/pip  
  
# Script de arranque  
COPY initial.py /solutions/  
RUN chmod 777 /solutions/initial.py && \  
chmod a+x /solutions/initial.py && \  
sed -i -e 's/\r$//' /solutions/initial.py  
  
# Volumenes para el python  
VOLUME /solutions/app  
  
# Configuracion supervisor  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]  

