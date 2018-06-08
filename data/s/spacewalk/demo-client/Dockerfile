FROM centos:7  
  
RUN yum install -y rhn-setup wget \  
&& wget http://yum.spacewalkproject.org/RPM-GPG-KEY-spacewalk-2015 \  
&& rpm --import RPM-GPG-KEY-spacewalk-2015 \  
&& wget https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7 \  
&& rpm --import RPM-GPG-KEY-EPEL-7 \  
&& yum update -y && yum clean all  
  
CMD "/usr/bin/bash"  

