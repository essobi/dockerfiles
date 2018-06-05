FROM centos:centos7  
  
RUN yum install -y epel-release  
RUN yum install -y \  
python-pip \  
python-devel \  
gcc \  
libffi-devel \  
openssl-devel \  
bind-utils \  
git \  
openssl \  
python-libcloud \  
rsync  
  
RUN pip install 'requests[security]' ansible~=2.4.0  
RUN yum install -y
https://releases.hashicorp.com/vagrant/2.0.4/vagrant_2.0.4_x86_64.rpm  
RUN vagrant plugin install vagrant-google  
  
CMD ansible  

