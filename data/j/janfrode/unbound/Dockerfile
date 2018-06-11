#  
FROM fedora:latest  
MAINTAINER Jan-Frode Myklebust <janfrode@tanso.net>  
  
RUN yum -y install unbound policycoreutils findutils iproute  
# Drop all setuid setgid permissions:  
RUN find /usr -perm /6000 -exec chmod -s '{}' \;  
RUN /usr/sbin/unbound-control-setup -d /etc/unbound/  
RUN /sbin/restorecon /etc/unbound/*  
RUN sed -i 's/# logfile: ""/logfile: ""/' /etc/unbound/unbound.conf  
RUN sed -i 's/# interface: 0.0.0.0/interface: 0.0.0.0/'
/etc/unbound/unbound.conf  
RUN sed -i 's/# access-control: 0.0.0.0\/0 refuse/access-control: 0.0.0.0\/0
allow/' /etc/unbound/unbound.conf  
#RUN ip address add 1.2.3.4/32 dev lo  
CMD ["/usr/sbin/unbound", "-v", "-v", "-d"]  
EXPOSE 53  
EXPOSE 53/udp  

