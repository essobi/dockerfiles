FROM centos:centos7  
ENV container docker  
RUN yum -y install \  
gcc \  
libffi-dev \  
libyaml-dev \  
libssl-dev \  
build-essential \  
libpython-dev \  
python \  
python-devel \  
python-virtualenv \  
python-setuptools \  
python-pip \  
aptitude \  
passwd \  
openssh \  
openssh-clients \  
openssh-server \  
gcc make \  
openssl-devel \  
sqlite-devel \  
bzip2-devel \  
rsyslog \  
sudo \  
wget \  
which \  
curl \  
git \  
git-core  
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm  
RUN yum install -y python36u python36u-libs python36u-devel python36u-pip  
RUN pip3.6 install --upgrade pip  
RUN pip3.6 install --upgrade setuptools  
RUN pip3.6 install ansible  
RUN pip3.6 install virtualenv  
RUN pip3.6 install tox  

