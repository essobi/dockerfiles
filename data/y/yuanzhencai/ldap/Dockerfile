# ldap  
#  
# OpenLDAP server  
#  
# Documentation:  
# - https://help.ubuntu.com/12.04/serverguide/openldap-server.html  
FROM yuanzhencai/ci-base  
MAINTAINER Yuan Zhencai <zhencai.yuan@datarx.cn>  
  
EXPOSE 389  
RUN yum -y install openldap-clients openldap-servers \  
&& yum -y clean all && rm -rf /var/cache/*  
  
# entrypoint script handles DB initialization  
COPY entrypoint.sh /entrypoint  
RUN chmod 700 /entrypoint  
  
# LDAP configuration parameters  
ENV organization ASF  
  
ENTRYPOINT ["/entrypoint"]  
CMD ["slapd", "-u", "ldap", "-h", "ldap:/// ldapi:///", "-F",
"/etc/openldap/slapd.d", "-d", "Stats"]  
  

