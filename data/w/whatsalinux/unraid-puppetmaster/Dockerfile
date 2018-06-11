FROM centos:7  
MAINTAINER dimitrius@gmail.com  
ENV container docker  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \  
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
VOLUME [ "/sys/fs/cgroup" ]  
CMD ["/usr/sbin/init"]  
  
COPY fastestmirror.conf /etc/yum/pluginconf.d  
RUN yum --disablerepo=epel || :  
RUN groupadd -g 5300 stack  
RUN rpm -Uvh http://yum.puppetlabs.com/puppet5/puppet5-release-el-7.noarch.rpm  
RUN rpm -Uvh http://yum.theforeman.org/releases/latest/el7/x86_64/foreman-
release.rpm  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum makecache fast || :  
RUN yum install -y yum-utils && yum-config-manager --enable centosplus >&
/dev/null  
RUN yum-config-manager --enable rhel-7-server-optional-rpms rhel-server-
rhscl-7-rpms  
RUN yum install -y foreman-installer  
RUN yum install -y vim git perl openssh-clients  
RUN /opt/puppetlabs/puppet/bin/gem install r10k  
RUN /opt/puppetlabs/puppet/bin/gem install yard  
RUN /opt/puppetlabs/puppet/bin/gem install puppet-strings  
  
## for sending mail  
RUN yum install -y mailx sendmail sendmail-cf  
RUN ln -s /bin/mailx /bin/email  
## set base mail config  
COPY mail.rc /etc/mail.rc  
## add user specific server and login  
RUN echo "set smtp=smtps://$SMTP_ADDRESS:$SMTP_PORT" >> /etc/mail.rc  
RUN echo "set smtp-auth-user=$SMTP_USER" >> /etc/mail.rc  
RUN echo "set smtp-auth-password=$SMTP_PASSWORD" >> /etc/mail.rc  
  
## fix domain  
COPY fixdomain.sh /tmp/fixdomain.sh  
RUN chmod 755 /tmp/fixdomain.sh  
RUN /tmp/fixdomain.sh  
  
## copy foreman answers file  
COPY foreman-answers.yaml /etc/foreman-installer/scenarios.d/foreman-
answers.yaml  
RUN chmod 600 /etc/foreman-installer/scenarios.d/foreman-answers.yaml  
## copy foreman-installer.sh  
COPY foreman-installer.sh /etc/foreman-installer/scenarios.d/foreman-
installer.sh  
RUN chmod 755 /etc/foreman-installer/scenarios.d/foreman-installer.sh  
RUN /etc/foreman-installer/scenarios.d/foreman-installer.sh  
  
## set stuff to autostart  
RUN systemctl enable puppetserver || :  
RUN systemctl enable foreman-proxy || :  
RUN systemctl enable httpd || :  
RUN systemctl enable sendmail || :  
  
## clean up yum  
RUN yum clean all  
COPY bashrc /home/puppet/.bashrc  
  
EXPOSE 8140 443 8444  
##entrypoints are more for "docker running one service"  
#ENTRYPOINT [ "/opt/puppetlabs/bin/puppetserver", "foreground"]  
## start processes  
#RUN systemctl start puppetserver || :  
#RUN systemctl start httpd || :  
#RUN systemctl foreman-proxy || :  

