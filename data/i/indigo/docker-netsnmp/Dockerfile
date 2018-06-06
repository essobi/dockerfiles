FROM centos:7  
MAINTAINER Ronny Trommer <ronny@opennms.org>  
  
ENV CONFIG /etc/sysconfig/snmpd  
ENV OPTIONS -LS0-6d  
  
RUN yum install -y net-snmp net-snmp-utils && \  
mkdir -p /etc/snmp/conf.d  
  
COPY config/snmpd.conf /etc/snmp/snmpd.conf  
COPY assets/* /etc/snmp/conf.d/  
  
ENTRYPOINT [ "/usr/sbin/snmpd" ]  
  
CMD [ "-f", "-LoS0-6d", "-c", "/etc/snmp/snmpd.conf" ]  
  
EXPOSE 161/udp  

