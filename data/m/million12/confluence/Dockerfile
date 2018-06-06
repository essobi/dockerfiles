FROM million12/centos-supervisor  
MAINTAINER Przemyslaw Ozgo linux@ozgo.info  
  
ENV CONFLUENCE_VERSION=5.9.6 \  
DB_SUPPORT=default  
  
RUN \  
rpm --rebuilddb && yum clean all && \  
yum install -y java-1.8.0-openjdk tar mariadb && \  
yum clean all  
  
COPY container-files/ /  

