FROM centos:latest  
  
RUN yum install -y dovecot dovecot-mysql mariadb  
  
COPY conf /etc/dovecot  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["app:start"]  

