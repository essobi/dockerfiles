FROM centos:centos6  
  
MAINTAINER Thomas Gerbet <thomas.gerbet@enalean.com>  
  
RUN yum install -y openssh-server \  
createrepo \  
epel-release \  
centos-release-scl \  
curl && \  
yum clean all  
  
COPY RPM-GPG-KEY.dag.txt /  
RUN rpm --import /RPM-GPG-KEY.dag.txt  
  
COPY rpmforge.repo /etc/yum.repos.d/  
COPY tuleap.repo /etc/yum.repos.d/  
COPY tuleap-local.repo /etc/yum.repos.d/  
  
COPY install.sh /install.sh  
COPY run.sh /run.sh  
RUN chmod u+x /run.sh && chmod u+x /install.sh  
  
VOLUME ["/output"]  
  
ENTRYPOINT ["/run.sh"]  

