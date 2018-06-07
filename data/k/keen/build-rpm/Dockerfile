FROM fedora:27  
MAINTAINER Greg Orzell <devops@keen.io>  
  
# Install base packages  
RUN dnf makecache && \  
dnf install -y \  
# Circle CI Requirements  
ca-certificates \  
git \  
gzip \  
openssh \  
openssh-clients \  
# RPM Tools and CLI depdencencies  
createrepo \  
curl \  
python-devel \  
python-pip \  
make \  
rpm-build && \  
dnf clean all  
  
# Install AWS/ECS CLI Tools  
RUN pip install --upgrade pip && \  
pip install setuptools && \  
pip install awscli  
  
CMD ["/bin/bash"]  

