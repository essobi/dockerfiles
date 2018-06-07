FROM fayehuang/centos  
MAINTAINER FayeHuang  
  
RUN yum -y install python-setuptools && yum clean all  
RUN easy_install pip && pip install supervisor  
  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 22  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

