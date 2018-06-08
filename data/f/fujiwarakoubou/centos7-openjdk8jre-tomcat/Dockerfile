FROM fujiwarakoubou/centos7-openjdk8jre  
  
# I'll have the usual.  
RUN yum -y update && yum clean all  
  
# Install tomcat  
RUN yum -y install tomcat && yum clean all  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  
  

