FROM centos:7  
MAINTAINER Frank Hildebrandt <fhildebrandt@freicon.de>  
  
RUN rpm -i https://packages.icinga.org/epel/7/release/noarch/icinga-rpm-
release-7-1.el7.centos.noarch.rpm \  
&& yum -y install epel-release \  
&& yum -y install icinga2 nagios-plugins-* \  
&& yum clean all  
  
RUN mkdir /run/icinga2 \  
&& chmod 777 /run/icinga2  
  
VOLUME /var/lib/icinga2  
VOLUME /var/cache/icinga2  
VOLUME /var/spool/icinga2  
VOLUME /var/log/icinga2  
  
CMD ["icinga2","daemon"]  
  
EXPOSE 5665

