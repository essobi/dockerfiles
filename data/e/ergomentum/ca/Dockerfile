FROM ergomentum/centos:7.3.161213211926  
MAINTAINER \  
Ergomentum <build@ergomentum.org>  
  
LABEL \  
vendor="Ergomentum" \  
license="Apache 2.0"  
  
RUN \  
# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1213602  
touch /var/lib/rpm/* && \  
yum install openssl && \  
yum clean all  
  
WORKDIR \  
/etc/pki/CA  
  
VOLUME \  
["/etc/pki/CA"]  
  
# Use two volumes for /etc/pki/tls/{certs,private}. Otherwise
/etc/pki/tls/openssl.cnf will not be visible.  
VOLUME \  
["/etc/pki/tls/certs"]  
  
VOLUME \  
["/etc/pki/tls/private"]  
  
COPY \  
common_functions.sh /  
COPY \  
entrypoint.sh /  
  
ENTRYPOINT \  
["/entrypoint.sh"]  

