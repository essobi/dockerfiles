FROM centos:6  
MAINTAINER Bertrand Roussel <broussel@sierrawireless.com>  
  
# Add EPEL  
RUN yum -y install epel-release  
  
# Add vmware-tools  
ENV VSPHERE_VERSION 5.5  
ADD vmware-tools.repo /etc/yum.repos.d/  
RUN sed -i "s/#VSPHERE_VERSION#/${VSPHERE_VERSION}/g" /etc/yum.repos.d/vmware-
tools.repo  
RUN yum install -y vmware-tools-esx-nox  
  
ADD scripts /etc/vmware-tools/scripts  
RUN chmod -R +x /etc/vmware-tools/scripts/*  
  
RUN sed -i "s/disable-tools-version=true/disable-tools-version=false/"
/etc/vmware-tools/tools.conf  
  
ADD sbin /usr/sbin  
  
ADD run-services.sh /  
RUN chmod +x /run-services.sh  
  
CMD /run-services.sh  
  

