FROM twistedogic/ambari-base  
MAINTAINER Jordan Li  
RUN yum install -y ambari-server  
RUN ambari-server setup --silent  
ADD start.sh /start.sh  
CMD /start.sh  

