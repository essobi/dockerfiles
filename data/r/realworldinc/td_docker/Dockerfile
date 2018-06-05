FROM centos:7  
ADD td.repo /etc/yum.repos.d/td-agent.repo  
ADD RPM-GPG-KEY-td-agent /etc/pki/rpm-gpg/RPM-GPG-KEY-td-agent  
  
RUN yum -q -y install td-agent gcc mysql-devel && yum clean all  
RUN td-agent-gem install fluent-plugin-mysql-appender  
  
ADD td-agent.conf /etc/td-agent/td-agent.conf  
  
CMD ["td-agent"]  

