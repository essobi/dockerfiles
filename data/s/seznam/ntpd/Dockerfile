FROM centos:7  
  
RUN yum install -y ntp && \  
yum -y clean all  
  
LABEL RUN="docker run -d --cap-add='SYS_TIME' --name NAME IMAGE" \  
STOP="docker stop NAME" \  
name="ntpd daemon" \  
vendor="Seznam.cz, a.s"  
  
ENTRYPOINT ["/usr/sbin/ntpd"]  
CMD ["-n", "-b", "-g", "-l", "stdout"]  

