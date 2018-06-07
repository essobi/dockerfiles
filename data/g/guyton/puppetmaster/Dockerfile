FROM guyton/centos6  
RUN yum install -y http://yum.puppetlabs.com/puppetlabs-release-
el-6.noarch.rpm  
RUN yum install -y puppet-3.8.7 ; yum clean all  
EXPOSE 8140  
CMD /usr/bin/puppet master --verbose --no-daemonize  

