FROM ubuntu:xenial  
  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
-y curl vim tar net-tools less slapd ldap-utils smbldap-tools samba  
  
# SAMBA schema import  
COPY files/smb-schema-import.sh /opt/smb-schema-import.sh  
RUN chmod 755 /opt/smb-schema-import.sh  
RUN /opt/smb-schema-import.sh  
  
COPY files/ldap-config.sh /opt/ldap-config.sh  
RUN chmod 755 /opt/ldap-config.sh  
  
COPY files/ldap-base.ldif /opt/ldap-base.ldif  
COPY files/ldap-base2.ldif /opt/ldap-base2.ldif  
  
COPY files/start.sh /opt/start.sh  
RUN chmod 755 /opt/start.sh  
  
ENTRYPOINT /opt/start.sh  

