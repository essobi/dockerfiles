FROM centos:7  
MAINTAINER Matthew Endsley <mendsley@gmail.com>  
  
# Install runit  
RUN yum install -y -q hostname  
RUN HOSTNAME=`hostname -f` && curl -s
"https://packagecloud.io/install/repositories/imeyer/runit/config_file.repo?os=el&dist=7&name=${HOSTNAME}"
> /etc/yum.repos.d/imeyer_runit.repo  
RUN yum install -y -q runit  
RUN yum clean all  
RUN rm -f /tmp/*  
  
ENTRYPOINT ["runsvdir", "-P", "-H", "/etc/service"]  

