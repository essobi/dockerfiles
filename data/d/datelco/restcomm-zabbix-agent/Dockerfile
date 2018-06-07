FROM datelco/zabbix-agent  
  
MAINTAINER gdubina@dataart.com  
  
ADD files/restcomm-zabbix-module.so /opt/restcomm-agent/restcomm-zabbix-
module.so  
ADD files/mesos-master-zabbix-module.so /opt/restcomm-agent/mesos-master-
zabbix-module.so  
  
RUN echo "LoadModulePath=/opt/restcomm-agent" >>
/etc/zabbix/zabbix_agentd.conf  
RUN echo "LoadModule=restcomm-zabbix-module.so" >>
/etc/zabbix/zabbix_agentd.conf  
RUN echo "LoadModule=mesos-master-zabbix-module.so" >>
/etc/zabbix/zabbix_agentd.conf  
  
ADD files/restcomm_conf.sh /etc/my_init.d/0_rescomm_module_conf.sh  
ADD files/mesos_conf.sh /etc/my_init.d/0_mesos_module_conf.sh  

