FROM sonatype/nexus3:3.2.0  
  
USER root  
  
RUN yum install -y sudo nfs-utils && \  
yum clean all  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

