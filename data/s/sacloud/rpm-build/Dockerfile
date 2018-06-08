FROM centos:7  
LABEL maintainer="Kazumichi Yamamoto <yamamoto.febc@gmail.com>"  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
  
RUN yum install -y \  
git \  
make \  
rpm-sign \  
createrepo \  
rpm-build \  
&& yum clean all  
  
ADD rpmmacros /root/.rpmmacros  
WORKDIR /workdir  
  
ADD sign_to_rpm.sh /sign_to_rpm.sh  
ADD sign_to_deb.sh /sign_to_deb.sh  
ENTRYPOINT ["rpmbuild"]

