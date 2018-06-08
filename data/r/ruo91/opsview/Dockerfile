#  
# Dockerfile - OPSVIEW  
#  
FROM centos:centos6  
MAINTAINER Yongbok Kim <ruo91@yongbok.net>  
  
# OPSVIEW  
ADD conf/opsview.repo /etc/yum.repos.d/opsview.repo  
RUN rpm -ivh http://pkgs.repoforge.org/rpmforge-release/rpmforge-
release-0.5.3-1.el6.rf.x86_64.rpm && rm -f rpmforge-
release-0.5.3-1.el6.rf.x86_64.rpm \  
&& yum update -y ; yum install -y opsview perl-DBIx-Class python-setuptools \  
&& service mysqld start && mysqladmin -u root password 'opsview' \  
&& sed -i 's/changeme/opsview/g' /usr/local/nagios/etc/opsview.conf \  
&& /usr/local/nagios/bin/db_mysql -u root -popsview \  
&& /usr/local/nagios/bin/db_opsview db_install \  
&& /usr/local/nagios/bin/db_runtime db_install \  
&& chmod -R 777 /var/log/opsview \  
&& /usr/local/nagios/bin/rc.opsview gen_config  
  
# Supervisord  
RUN easy_install pip && pip install supervisor && pip install
virtualenvwrapper \  
&& echo 'export WORKON_HOME=$HOME/.virtualenvs' >> /root/.bashrc \  
&& echo 'source /usr/bin/virtualenvwrapper.sh' >> /root/.bashrc \  
&& mkdir /etc/supervisord.d  
ADD conf/supervisord.conf /etc/supervisord.d/supervisord.conf  
  
# Supervisord  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.d/supervisord.conf"]  
  
# Port  
EXPOSE 3000  

