FROM centos:7  
# Which git commit of rancid-git do we build against?  
ENV hash=400d6121da6ba5d9cc5f3ad49270071dcb8c4674  
  
# epel-release is now available in centos-extras (enabled by default)  
RUN yum -y install epel-release  
  
# basic dev env  
RUN yum -y install \  
bash-completion \  
git \  
make \  
rpmdevtools \  
tar\  
tito \  
yum-utils \  
&& yum clean all  
  
# create /rpmbuild tree  
RUN rpmdev-setuptree  
  
# download sysconftool srpm from fedora 20 and build for centos  
ADD build_sysconftool.sh /tmp/  
RUN /tmp/build_sysconftool.sh  
  
# build rancid-git  
RUN cd /root && \  
git clone https://github.com/dotwaffle/rancid-git.git && \  
cd rancid-git && \  
git checkout ${hash} -b old_commit && \  
yum-builddep -y rancid-git.spec && \  
tito build --rpm --test  
  
# install rancid-git  
RUN yum -y localinstall /tmp/tito/x86_64/rancid-git-*.el7.centos.x86_64.rpm  

