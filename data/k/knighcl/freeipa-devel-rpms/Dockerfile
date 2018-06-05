FROM fedora:rawhide  
MAINTAINER Curtis L. Knight  
  
# update base image  
RUN yum -y update && yum clean all  
  
# install git and rpm build tools  
RUN yum -y install git yum-utils make rpmdevtools rpmlint cpp pylint  
  
ADD freeipa-devel-rpm-build /usr/sbin/freeipa-devel-rpm-build  
RUN chmod -v +x /usr/sbin/freeipa-devel-rpm-build  
CMD ["master"]  
ENTRYPOINT ["/usr/sbin/freeipa-devel-rpm-build"]  
  

