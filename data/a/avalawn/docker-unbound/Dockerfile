FROM centos:centos6  
RUN rpm -i http://www.gtlib.gatech.edu/pub/fedora-epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN yum install unbound -y  
RUN /usr/sbin/unbound-control-setup -d /etc/unbound/  
  
EXPOSE 53  
EXPOSE 53/udp  
  
CMD ["/usr/sbin/unbound", "-d", "-v", "-v", "-c", "/etc/unbound/unbound.conf"]  

