FROM centos  
MAINTAINER martin scharm <https://binfalse.de>  
  
RUN yum -y update && \  
yum -y install epel-release && \  
yum -y install http://packages.icinga.org/epel/7/release/noarch/icinga-rpm-
release-7-1.el7.centos.noarch.rpm && \  
yum -y install vim hostname bind-utils cronie mailx mariadb && \  
yum -y install --enablerepo=icinga-snapshot-builds icinga2 icinga2-ido-mysql
icingacli nagios-plugins-all && \  
yum clean all  
  
COPY run.sh /  
EXPOSE 5665  
ENTRYPOINT [ "/run.sh" ]  

