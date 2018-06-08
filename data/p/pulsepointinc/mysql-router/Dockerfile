FROM centos:7  
COPY files/etc/yum.repos.d/mysql-tools-community.repo /etc/yum.repos.d/  
  
COPY files/etc/pki/rpm-gpg/RPM-GPG-KEY-mysql /etc/pki/rpm-gpg/  
  
RUN \  
yum --disablerepo="*" \--enablerep="mysql-tools-community" install -y mysql-
router-2.1.3 && \  
yum clean all  
  
COPY files/start.sh /  
  
CMD ["/start.sh"]  

