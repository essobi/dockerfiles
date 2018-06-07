FROM qnib/terminal  
  
RUN yum install -y python-zmq python-pip libyaml-devel python-devel && \  
pip install neo4jrestclient pyyaml docopt  
ADD etc/supervisord.d/inventory.ini /etc/supervisord.d/  
ADD opt/qnib/inventory/bin/inventory.py /opt/qnib/inventory/bin/  
ADD etc/consul.d/check_inv.json /etc/consul.d/  

