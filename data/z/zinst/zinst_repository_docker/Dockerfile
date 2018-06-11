FROM centos:7  
LABEL version=0.6  
RUN yum install -y bc sudo which crontabs.noarch tar  
  
RUN curl -sL bit.ly/zinst-install |bash  
RUN zinst i zinst_simple_server -stable 2> /dev/null  
  
RUN yum clean all; yum clean all  
  
COPY entrypoint.sh /data/bin/entrypoint.sh  
RUN chmod 755 /data/bin/entrypoint.sh  
  
ENTRYPOINT [ "/data/bin/entrypoint.sh" ]  
EXPOSE 80  

