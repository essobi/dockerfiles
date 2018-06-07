FROM fayehuang/centos-http  
MAINTAINER FayeHuang  
  
RUN yum install -y createrepo yum-arch yum-downloadonly && yum clean all  
WORKDIR /var/www/html  
COPY supervisord.conf /etc/supervisord.conf  
EXPOSE 80 22  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

