FROM centos:7  
MAINTAINER Chris Straffon <muppet_3000@hotmail.com>  
  
RUN yum update -y && yum install -y dhcp && yum clean all  
  
EXPOSE 67  
EXPOSE 68  
VOLUME ["/etc/dhcp"]  
  
CMD /usr/sbin/dhcpd -d -cf /etc/dhcp/dhcpd.conf  
  

