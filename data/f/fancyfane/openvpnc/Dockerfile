FROM centos:latest  
MAINTAINER FancyFane me@jasonfane.com  
  
RUN yum update -y && \  
yum install epel-release -y && \  
yum install openvpn -y && \  
yum clean all && \  
rm -rf /var/cache/yum && \  
mkdir /vpn  
  
VOLUME ["/vpn"]  
ENTRYPOINT ["openvpn"]  
CMD [ "--config", "/vpn/vpn.conf" , "--script-security", "2" ]  

