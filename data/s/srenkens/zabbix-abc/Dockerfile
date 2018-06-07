FROM berngp/docker-zabbix  
MAINTAINER Sebastiaan Renkens <sebastiaan.renkens@ordina.nl>  
  
# Refresh  
RUN yum makecache  
  
# Perform update first  
RUN yum update -y  
  
# Add php pear Mail packages to enable mail functionality in custom alert
scripts  
RUN yum -y install php-pear-Mail  
  
# YUM Cleanup  
RUN yum clean all && rm -rf /tmp/*  
  
# Install curl version with openssl instead of NSS to enable TLS 1.1 and TLS
1.2 support  
COPY ./rpms/curl-7.19.7-41.perk.el6.x86_64.rpm
/tmp/curl-7.19.7-41.perk.el6.x86_64.rpm  
COPY ./rpms/libcurl-7.19.7-41.perk.el6.x86_64.rpm
/tmp/libcurl-7.19.7-41.perk.el6.x86_64.rpm  
RUN rpm -Uvh --force /tmp/curl-7.19.7-41.perk.el6.x86_64.rpm
/tmp/libcurl-7.19.7-41.perk.el6.x86_64.rpm  
  
# Add extra trusted root certificates to /etc/pki/tls/certs/ca-bundle.crt  
COPY ./pki/trusted-certs /tmp/trusted-certs  
RUN cat /tmp/trusted-certs >> /etc/pki/tls/certs/ca-bundle.crt

