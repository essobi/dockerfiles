FROM centos:7  
LABEL maintainer "Fabio Montefuscolo<fabio.montefuscolo@gmail.com>"  
  
RUN yum install rpm-build rpmdevtools -y \  
&& yum --enablerepo=* clean all \  
&& rm -rf /var/cache/yum  
  
ENV RPM_BUILD_ROOT=/root/rpmbuild  
  
VOLUME $RPM_BUILD_ROOT  
WORKDIR $RPM_BUILD_ROOT  
  
ADD root/ /  
CMD ["/bin/bash"]  

