FROM centos:latest  
  
RUN yum install -y createrepo && yum clean all  
  
VOLUME /data  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD [ "createrepo" ]

