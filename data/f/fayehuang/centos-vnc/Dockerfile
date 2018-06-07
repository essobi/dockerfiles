FROM fayehuang/centos-supervisor  
MAINTAINER FayeHuang  
  
RUN yum groupinstall -y Desktop  
RUN yum install -y tigervnc-server firefox fonts-chinese && yum clean all  
  
COPY vnc_init.sh /root/vnc_init.sh  
RUN chmod +x /root/vnc_init.sh  
  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 5900 22  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  
  

