FROM alpine:3.6  
LABEL maintainer "Tonnerre LOMBARD <tonnerre@ancient-solutions.com>"  
  
RUN apk --update add openldap-clients openldap openldap-back-hdb openldap-
back-bdb python3 py3-jinja2  
  
RUN install -o ldap -g ldap -m 0775 -d /etc/openldap/slapd.d
/var/lib/openldap/run  
COPY ["schema/krb5-kdc.schema", "schema/ngas.schema", "schema/solaris.schema",
"/etc/openldap/schema/"]  
COPY ["templates", "/etc/openldap/templates"]  
COPY ["slapd_launcher.py", "/usr/local/bin/slapd_launcher.py"]  
  
EXPOSE 1636/tcp  
USER ldap  
VOLUME ["/secret/ldap_root_pw", "/secret/ldap_syncrepl_pw", "/ssl", "/sslca",
"/var/lib/openldap/openldap-data"]  
  
ENTRYPOINT ["/usr/bin/python3", "/usr/local/bin/slapd_launcher.py"]  

