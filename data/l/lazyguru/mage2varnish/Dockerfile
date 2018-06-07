FROM lazyguru/mage2base  
  
# Installing Varnish  
RUN yum -y upgrade ca-certificates  
RUN yum -y install https://repo.varnish-cache.org/redhat/varnish-4.0.el6.rpm  
RUN yum -y install epel-release  
RUN yum -y install varnish  
  
RUN mv /etc/sysconfig/varnish /etc/sysconfig/default.varnish  
ADD etc/varnish.conf/varnish /etc/sysconfig/varnish  
ADD etc/varnish.conf/default.vcl /etc/varnish/default.vcl  
  
ADD scripts/start.sh /start.sh  
RUN chmod 755 /start.sh  
  
EXPOSE 80  
EXPOSE 6082  
CMD ["/bin/bash", "/start.sh" ]  

