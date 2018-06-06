FROM centos:7  
COPY curator.repo /etc/yum.repos.d/  
  
RUN yum install elasticsearch-curator -y \  
&& yum clean all  
  
ENV LC_ALL=en_US.utf-8 LANG=en_US.utf-8  
WORKDIR /mian  
  
COPY config.yml config.yml  
COPY action.yml action.yml  
  
ENTRYPOINT [ "curator", "--config", "config.yml", "action.yml" ]

