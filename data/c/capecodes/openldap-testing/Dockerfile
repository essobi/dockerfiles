FROM osixia/openldap:1.1.8  
MAINTAINER Cape Codes <info@cape.codes>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update &&
DEBIAN_FRONTEND=noninteractive && DEBIAN_FRONTEND=noninteractive apt-get
install -yq vim less openssl inetutils-ping net-tools &&
DEBIAN_FRONTEND=noninteractive apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
ENV LDAP_TLS_VERIFY_CLIENT try  
  
ENV LDAP_TLS_CRT_FILENAME server.crt  
ENV LDAP_TLS_KEY_FILENAME server.key  
ENV LDAP_TLS_CA_CRT_FILENAME ca.crt  
  
ENV LDAP_ORGANISATION Example Inc.  
ENV LDAP_DOMAIN example.org  
  
ENV LDAP_ADMIN_PASSWORD password  
ENV LDAP_CONFIG_PASSWORD password  
ENV LDAP_READONLY_USER true  
ENV LDAP_READONLY_USER_PASSWORD password  
  
ENV LDAPTLS_CACERT=/container/service/slapd/assets/certs/ca.crt  
  
RUN mkdir -p /container/service/slapd/assets/config  
  
ADD bootstrap /container/service/slapd/assets/config/bootstrap  
ADD certs /container/service/slapd/assets/certs  

