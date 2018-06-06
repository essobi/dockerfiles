FROM centos:centos7  
RUN yum install -y gettext && yum clean all -y  
  
COPY "nexus-configure" "/nexus-configure"  
WORKDIR "/nexus-configure"  
RUN chmod +x /nexus-configure/main.sh  
ENTRYPOINT "/nexus-configure/main.sh"  
  
ENV NEXUS_URL="http://localhost:8081"  
ENV NEXUS_USER="admin"  
ENV NEXUS_PASS="admin123"  

