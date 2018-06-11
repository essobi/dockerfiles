FROM centos:centos7  
  
RUN echo "exclude=filesystem*" >> /etc/yum.conf  
  
RUN yum clean all \  
&& yum install yum-plugin-ovl -y \  
&& yum update -y \  
&& yum clean all \  
&& rm -rf /var/cache/yum \  
&& rpm --rebuilddb  
  
ONBUILD RUN yum clean all \  
&& yum update -y \  
&& yum clean all \  
&& rm -rf /var/cache/yum \  
&& rpm --rebuilddb  

