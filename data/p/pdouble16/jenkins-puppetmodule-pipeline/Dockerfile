FROM pdouble16/jenkins-puppetmodule-pipeline:centos7  
MAINTAINER Patrick Double <pat@patdouble.com>  
  
# systemd support: https://github.com/docker-library/docs/tree/master/centos  
ENV container docker  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
VOLUME [ "/sys/fs/cgroup" ]  
  
WORKDIR /puppet  
COPY manifests/ /puppet/jenkins_puppetmodule_pipeline/manifests/  
COPY templates/ /puppet/jenkins_puppetmodule_pipeline/templates/  
COPY README.md metadata.json Puppetfile.lock Gemfile
/puppet/jenkins_puppetmodule_pipeline/  
  
COPY containers/Puppetfile /puppet/  
COPY examples/public_projects.pp /puppet/  
RUN source /etc/profile.d/rbenv.sh && librarian-puppet install --verbose  
RUN source /etc/profile.d/rbenv.sh && puppet apply -e 'include
jenkins_puppetmodule_pipeline::jenkins' \--debug --modulepath=/puppet/modules  
RUN source /etc/profile.d/rbenv.sh && puppet apply -e 'include
jenkins_puppetmodule_pipeline::groovy' \--debug --modulepath=/puppet/modules  
RUN source /etc/profile.d/rbenv.sh && puppet apply -e 'include
jenkins_puppetmodule_pipeline::plugins' \--debug --modulepath=/puppet/modules  
RUN source /etc/profile.d/rbenv.sh && puppet apply -e 'include
jenkins_puppetmodule_pipeline' \--debug --modulepath=/puppet/modules  
  
VOLUME ["/var/lib/jenkins"]  
EXPOSE 8080  
  
CMD ["/usr/sbin/init"]  

