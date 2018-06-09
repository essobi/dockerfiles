FROM centos:6  
MAINTAINER Xavier Gouardes <xavier.gouardes@laposte.net>  
  
LABEL name="OpenLdap Region" \  
vendor="xtechnologies" \  
license="GPLv2" \  
build-date="2016-03-02"  
  
RUN yum -y update && \  
yum -y install openldap openldap-clients openldap-servers rsyslog httpd php
php-ldap  
  
# RUN chkconfig rsyslog on ; chkconfig slapd on ; chkconfig httpd on ; service
rsyslog start  
RUN cd /etc/rsyslog.d && echo "local4.* /var/log/ldap.log" > slapd.conf  
  
COPY olcDatabase={1}monitor.ldif /etc/openldap/slapd.d/cn=config  
COPY olcDatabase={2}bdb.ldif /etc/openldap/slapd.d/cn=config  
COPY init-ldap.ldif /tmp  
COPY config.php /tmp  
COPY phpldapadmin-1.2.3.tgz /var/www/html  
  
RUN chown -R ldap:ldap /etc/openldap ; service slapd start ; ldapadd -v -x -f
/tmp/init-ldap.ldif -D "cn=ldap-manager,dc=ma-region,dc=fr" -w toto  
RUN cd /var/www/html ; tar xzvf phpldapadmin-1.2.3.tgz ; mv phpldapadmin-1.2.3
ldapadmin ; cp /tmp/config.php ldapadmin/config  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80 389  
CMD ["/bin/bash"]  
  

