FROM centos:7  
  
RUN curl -L http://kimchi-
project.github.io/ginger/downloads/latest/ginger.el7.centos.noarch.rpm -o
/tmp/ginger.el7.centos.noarch.rpm; curl -L http://github.com/kimchi-
project/wok/releases/download/2.5.0/wok-2.5.0-0.el7.centos.noarch.rpm -o
/tmp/wok.el7.centos.noarch.rpm;curl -L http://kimchi-
project.github.io/gingerbase/downloads/latest/ginger-
base.el7.centos.noarch.rpm -o /tmp/ginger-base.el7.centos.noarch.rpm; curl -L
https://github.com/kimchi-
project/kimchi/releases/download/2.5.0/kimchi-2.5.0-0.el7.centos.noarch.rpm -o
/tmp/kimchi.el7.centos.noarch.rpm;curl -L
https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm -o
/tmp/epel-release-latest-7.noarch.rpm  
  
RUN yum -y install /tmp/epel-release-latest-7.noarch.rpm  
  
RUN yum -y update  
  
RUN yum -y install /tmp/wok.el7.centos.noarch.rpm /tmp/ginger-
base.el7.centos.noarch.rpm /tmp/ginger.el7.centos.noarch.rpm
/tmp/kimchi.el7.centos.noarch.rpm  
  
EXPOSE 8001  
CMD ["/bin/wokd"]  

