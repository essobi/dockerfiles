FROM centos:centos6  
  
MAINTAINER nmcspadden@gmail.com  
  
ENV PUPPET_VERSION 3.7.4  
RUN rpm --import https://yum.puppetlabs.com/RPM-GPG-KEY-puppetlabs && rpm -ivh
http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm  
RUN yum install -y yum-utils && yum-config-manager --enable centosplus >&
/dev/null  
RUN yum install -y puppet-$PUPPET_VERSION  
RUN yum install -y puppet-server-$PUPPET_VERSION  
RUN yum clean all  
ADD puppet.conf /etc/puppet/puppet.conf  
  
VOLUME ["/opt/puppet"]  
  
RUN cp -rf /etc/puppet/* /opt/puppet/  
  
VOLUME ["/opt/varpuppet/lib/puppet"]  
  
RUN cp -rf /var/lib/puppet/* /opt/varpuppet/lib/puppet/  
  
EXPOSE 8140  
ENTRYPOINT [ "/usr/bin/puppet", "master", "--no-daemonize", "--verbose" ]  

