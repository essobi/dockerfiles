FROM centos/systemd  
  
RUN yum -y install
https://ftp.ripe.net/tools/rpki/validator3/rc/centos7/repo/rpki-
validator-3.0-286.noarch.rpm  
RUN systemctl enable rpki-validator-3.service  
  
EXPOSE 8080  
CMD ["/usr/sbin/init"]  

