FROM sonatype/nexus3:3.0.2  
  
USER root  
RUN yum -y install epel-release && \  
yum -y install jq && \  
yum clean all  
USER nexus  
  
ADD configure.sh /usr/local/bin/  

