FROM centos:6  
MAINTAINER Jamie Curnow <jc@jc21.com>  
LABEL maintainer="Jamie Curnow <jc@jc21.com>"  
  
# Yum  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm && \  
yum -y update && \  
yum -y install rpmdevtools mock rpmlint git wget curl kernel-devel rpmdevtools
rpmlint rpm-build sudo gcc-c++ make automake autoconf expect  
  
# build files  
ADD bin/build-spec /bin/  
ADD bin/build-all /bin/  
  
# Sudo  
ADD etc/sudoers.d/wheel /etc/sudoers.d/  
RUN chown root:root /etc/sudoers.d/*  
  
# Remove requiretty from sudoers main file  
RUN sed -i '/Defaults requiretty/c\\#Defaults requiretty' /etc/sudoers  
  
# Rpm User  
RUN adduser -G wheel rpmbuilder \  
&& mkdir -p
/home/rpmbuilder/rpmbuild/{BUILD,SPECS,SOURCES,BUILDROOT,RPMS,SRPMS,tmp} \  
&& chmod -R 777 /home/rpmbuilder/rpmbuild  
  
ADD .rpmmacros /home/rpmbuilder/  
USER rpmbuilder  
  
WORKDIR /home/rpmbuilder  

