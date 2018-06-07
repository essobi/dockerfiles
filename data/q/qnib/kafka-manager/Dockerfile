FROM qnib/u-java8  
  
ENV KM_VER=1.3.0.8 \  
ZOOKEEPER_HOSTS=zookeeper.service.consul:2181  
RUN apt-get install -y wget nmap \  
&& wget -qO /tmp/kafka-manager_${KM_VER}_all.deb
https://github.com/qnib/kafka-manager/releases/download/${KM_VER}/kafka-
manager_${KM_VER}_all.deb \  
&& dpkg -i /tmp/kafka-manager_${KM_VER}_all.deb \  
&& rm -f /tmp/kafka-manager_${KM_VER}_all.deb  
ADD etc/supervisord.d/kafka-manager.ini /etc/supervisord.d/  
ADD opt/qnib/kafka/manager/bin/start.sh \  
opt/qnib/kafka/manager/bin/healthcheck.sh \  
/opt/qnib/kafka/manager/bin/  
ADD etc/consul.d/kafka-manager.json /etc/consul.d/  
ADD etc/consul-templates/kafka/manager/application.conf.ctmpl /etc/consul-
templates/kafka/manager/  

