FROM registry.access.redhat.com/rhel7  
MAINTAINER Eduardo Minguez <e.minguez@gmail.com>  
  
RUN yum localinstall -y
http://pkgs.repoforge.org/stress/stress-1.0.2-1.el7.rf.x86_64.rpm  
  
ENTRYPOINT ["/usr/bin/stress", "--verbose"]  
CMD []  

