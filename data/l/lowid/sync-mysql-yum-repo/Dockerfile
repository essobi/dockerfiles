FROM centos:7  
RUN yum -y install epel-release \  
&& yum -y install reposync createrepo \  
&& yum --enablerepo=* clean all \  
&& rm -rf /var/cache/yum \  
&& rm -f /etc/yum.repos.d/*.repo  
  
COPY mysql-56-repo.conf /opt/  
COPY syncrepo.sh /opt/  
  
RUN chmod 750 /opt/syncrepo.sh  
  
RUN mkdir -p /repos  
VOLUME ["/repos"]  
  
ENTRYPOINT ["/bin/bash", "/opt/syncrepo.sh"]  

