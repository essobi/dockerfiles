FROM centos  
  
RUN yum install -y \  
epel-release \  
&& yum install -y \  
rpmdevtools \  
rpm-build \  
automake \  
libtool \  
make \  
selinux-policy-devel \  
selinux-policy-doc \  
&& yum clean all  
  
COPY build-rpm-package.sh \  
create-source-tarball.sh \  
/usr/local/bin/  
  
WORKDIR /git  

