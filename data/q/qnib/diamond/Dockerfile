###### QNIBTerminal images  
FROM qnib/sensu  
  
ENV SENSU_CLIENT=true  
  
RUN yum install -y --nogpgcheck gcc python-devel python-configobj lm_sensors
python-pip && \  
pip install --upgrade pip && \  
pip install diamond pysensors && \  
rm -rf /etc/diamond && mkdir -p /var/log/diamond  
ADD etc/diamond /etc/diamond  
ADD opt/qnib/diamond/bin/start.sh /opt/qnib/diamond/bin/  
ADD etc/supervisord.d/diamond.ini /etc/supervisord.d/diamond.ini  
ADD etc/consul.d/diamond.json /etc/consul.d/  

