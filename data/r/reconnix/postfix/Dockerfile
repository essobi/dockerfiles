### Dockerfile  
FROM reconnix/base:latest  
MAINTAINER Russ McKendrick <russ.mckendrick@reconnix.com>  
  
RUN yum -y install rsyslog postfix python-setuptools && yum clean all  
RUN easy_install pip && pip install "pip>=1.4,<1.5" \--upgrade && pip install
supervisor  
ADD conf-supervisord.conf /etc/supervisord.conf  
ADD run /usr/local/bin/  
RUN chmod +x /usr/local/bin/run  
ADD rsyslog.conf /etc/  
CMD ["/usr/local/bin/run"]

