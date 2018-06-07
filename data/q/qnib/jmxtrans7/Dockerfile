###### QNIBTerminal child  
FROM qnib/java7  
  
RUN export JMX_VER=251 && \  
yum install -y
http://central.maven.org/maven2/org/jmxtrans/jmxtrans/${JMX_VER}/jmxtrans-${JMX_VER}.rpm
&& \  
unset JMX_VER  
ADD opt/qnib/jmxtrans/bin/start.sh /opt/qnib/jmxtrans/bin/  
ADD etc/supervisord.d/jmxtrans.ini /etc/supervisord.d/  
ADD var/lib/jmxtrans/jvm.json /var/lib/jmxtrans/  
ADD etc/consul-templates/*.ctmpl /etc/consul-templates/  

