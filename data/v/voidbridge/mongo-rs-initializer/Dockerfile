FROM voidbridge/centos7  
MAINTAINER Voidbridge <developers@voidbridge.com>  
  
ADD files/etc/yum.repos.d /etc/yum.repos.d  
RUN yum install -y \--enablerepo=centosplus gettext epel-release && \  
yum install -y mongodb-org hostname bind-utils python-pip && \  
pip install j2cli && \  
yum clean all -y  
  
ADD files /  
RUN chmod 755 /opt/mongo-rs-initializer/initialize.sh  
  
USER 1001  
CMD ["/opt/mongo-rs-initializer/initialize.sh"]

