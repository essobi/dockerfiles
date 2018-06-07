FROM centos:latest  
  
RUN yum install -y samba && \  
yum clean all  
  
COPY samba.sh /bin/samba.sh  
  
EXPOSE 137/udp 138/udp 139 445  
ENTRYPOINT ["samba.sh"]  

