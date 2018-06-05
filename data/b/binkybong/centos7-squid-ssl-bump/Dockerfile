FROM centos:7  
MAINTAINER Andy Wong pslandywong@hotmail.com  
  
RUN yum -y install epel-release  
  
RUN yum -y install squid squid-helpers openssl httpd-tools vim wget curl git
&& yum -y clean all  
  
COPY squid-config/squid.ssl.conf /etc/squid/squid.ssl.conf  
  
COPY squid-config/ssl.pem /etc/squid/ssl.pem  
  
# create squid cache dirs  
RUN /usr/sbin/squid -N -z -f /etc/squid/squid.ssl.conf  
  
# create ssl_crtd working dir  
RUN /usr/lib64/squid/ssl_crtd -c -s /var/spool/squid/ssl_db  
  
RUN chmod a+r /var/spool/squid/ssl_db  
  
RUN chmod a+r /etc/squid/*  
  
RUN chown -R squid:squid /etc/squid /var/spool/squid  
  
EXPOSE 3128  
VOLUME ["/var/log"]  
  
CMD ["/usr/sbin/squid", "-N", "-f", "/etc/squid/squid.ssl.conf"]  

