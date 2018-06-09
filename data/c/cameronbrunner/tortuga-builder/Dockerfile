FROM centos:7  
RUN rpm -ivh http://yum.puppetlabs.com/puppet5/puppet5-release-el-7.noarch.rpm
&& \  
yum install -y centos-release-scl puppet-agent && \  
yum install -y rh-python36 git rsync bzip2 && \  
rm -rf /var/cache/yum  
ADD scripts/entrypoint.sh /  
ADD scripts/build-tortuga.sh /  
ENTRYPOINT [ "/entrypoint.sh" ]  

