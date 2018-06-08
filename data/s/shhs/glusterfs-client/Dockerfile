FROM centos:latest  
MAINTAINER SHS <shs@overstack.ru>  
  
RUN yum -y update && \  
yum -y -q install glusterfs glusterfs-fuse attr && \  
yum clean all  
  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["bash"]  

