FROM fedora:latest  
  
RUN /usr/bin/dnf check-update || echo "Update available"  
RUN /usr/bin/dnf upgrade -y  
RUN /usr/bin/dnf install -y openldap-clients openldap-servers smbldap-tools  
RUN /usr/bin/rm -fr /etc/openldap/slapd.d /var/lib/ldap  
RUN /usr/bin/mkdir -pv /etc/openldap/slapd.d /var/lib/ldap  
  
COPY slapd-conf /var/tmp/slapd-conf/  
COPY openldap-entrypoint.sh /  
  
# Expose ldap  
EXPOSE 389 636  
ENTRYPOINT ["/openldap-entrypoint.sh"]  
  
# LDAP dir  
VOLUME ["/var/lib/ldap"]  
VOLUME ["/etc/openldap/slapd.d"]  

