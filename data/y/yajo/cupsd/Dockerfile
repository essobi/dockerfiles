FROM centos  
  
MAINTAINER yajo@openaliasbox.org  
  
CMD ["cupsd", "-f"]  
  
EXPOSE 631  
VOLUME /var/log/cups /var/run/cups  
  
# OpenSSL is used to autogenerate SSL certs  
RUN yum -y install cups hostname openssl && \  
  
# Need to install CUPS with docs, or the web page will fail with "Not Found"  
yum -y --setopt tsflags= reinstall cups && \  
  
yum clean all  
  
ADD *.conf passwd.md5 /etc/cups/  
  
# Customize cupsd to install printers before launching  
ADD custom-cupsd.sh /usr/local/sbin/cupsd  

