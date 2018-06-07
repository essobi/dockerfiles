FROM osixia/openldap  
  
RUN rm -fr /var/lib/ldap && rm -fr /etc/ldap/slapd.d  
  
COPY ./data /var/lib/ldap  
COPY ./config /etc/ldap/slapd.d  
  
RUN chown -R openldap:openldap /var/lib/ldap && chown -R openldap:openldap
/etc/ldap/slapd.d  

