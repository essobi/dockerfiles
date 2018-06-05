FROM extvos/centos  
  
MAINTAINER "Mingcai SHEN <archsh@gmail.com>"  
ENV CACTI_VERSION 0.8.8f  
  
COPY start-service.sh /  
COPY packages/cacti.conf /etc/httpd/conf.d/  
  
RUN yum install -y httpd mod_ssl cronie \  
&& yum install -y php php-mysql php-snmp php-ldap php-xml php-gd php-snmp pcre
net-snmp net-snmp-libs net-snmp-utils wget patch \  
&& chmod +x /start-service.sh \  
&& cd /opt \  
&& wget http://www.cacti.net/downloads/cacti-${CACTI_VERSION}.tar.gz \  
&& tar zxf cacti-${CACTI_VERSION}.tar.gz \  
&& rm -f cacti-${CACTI_VERSION}.tar.gz \  
&& ln -s /opt/cacti-${CACTI_VERSION} /opt/cacti \  
&& cp /opt/cacti/include/config.php /opt/cacti/include/config.php.default  
  
  
EXPOSE 80  
VOLUME ["/opt/cacti/rra", "/opt/cacti/log"]  
  
CMD ["/start-service.sh"]

