FROM centos:7  
MAINTAINER mario@mancino-net.de  
  
# RHEL packages  
RUN yum install -y python python-setuptools wget python-ldap python-netaddr
python-pyasn1 python-pyasn1-modules python-pillow python-dns; yum clean all  
  
# Python modules  
RUN easy_install pyweblib; easy_install pyexcelerator  
  
# Download and install web2ldap  
RUN wget https://www.web2ldap.de/download/web2ldap-1.2.78.tar.gz; tar xzf
web2ldap-1.2.78.tar.gz --no-same-owner; mv web2ldap-1.2.78 /opt/web2ldap; rm
web2ldap-1.2.78.tar.gz  
  
# Allow Access from all IP's  
RUN sed -i -- "s|access_allowed = \\[.*|access_allowed =
\\['0.0.0.0/0.0.0.0',|g" /opt/web2ldap/etc/web2ldap/web2ldapcnf/standalone.py  
  
# Clear Pre-Configured LDAP hosts  
RUN echo "ldap_uri_list=[('ldap://127.0.0.1:1390', u'Local OpenLDAP 2.x
Server')]" >> /opt/web2ldap/etc/web2ldap/web2ldapcnf/hosts.py; echo
"restricted_ldap_uri_list = 1" >>
/opt/web2ldap/etc/web2ldap/web2ldapcnf/hosts.py  
  
# Expose Port  
EXPOSE 1760  
# Start Service  
CMD ["/usr/bin/python", "/opt/web2ldap/sbin/web2ldap.py", "-l",
"0.0.0.0:1760", "-d", "off"]  

