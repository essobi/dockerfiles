FROM centos:centos6  
MAINTAINER pepechoko  
  
RUN yum update -y \  
&& yum clean all  
  
RUN \  
rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
  
RUN yum install -y \  
autoconf \  
automake \  
curl-devel \  
gcc \  
gcc-c++ \  
git \  
libxml2-devel \  
libxslt-devel \  
libyaml-devel \  
make \  
mysql-devel \  
openssh \  
openssh-clients \  
openssh-server \  
openssl-devel \  
passwd \  
readline-devel \  
sqlite-devel \  
sudo \  
tar \  
tree \  
which \  
zlib-devel \  
&& yum clean all  
  
# Install rbenv  
RUN \  
groupadd rbenv && \  
cd /usr/local && \  
git clone https://github.com/sstephenson/rbenv.git && \  
chgrp -R rbenv /usr/local/rbenv && \  
chmod -R g+rwxXs /usr/local/rbenv  
  
# Install ruby-build  
RUN \  
mkdir /usr/local/rbenv/plugins && \  
cd /usr/local/rbenv/plugins && \  
git clone https://github.com/sstephenson/ruby-build.git && \  
chgrp -R rbenv /usr/local/rbenv/plugins/ruby-build && \  
chmod -R g+rwxXs /usr/local/rbenv/plugins/ruby-build && \  
cd /usr/local/rbenv/plugins/ruby-build && \  
./install.sh  
  
ENV RBENV_ROOT /usr/local/rbenv  
ENV PATH /usr/local/rbenv/bin:$PATH  
ADD rbenv.sh /etc/profile.d/rbenv.sh  
RUN chmod +x /etc/profile.d/rbenv.sh  
  
# install rbenv-default-gems  
RUN \  
cd /usr/local/rbenv/plugins && \  
git clone git://github.com/sstephenson/rbenv-default-gems.git  
  
ADD ./default-gems /usr/local/rbenv/default-gems  
  
# install rbevn-binstub  
RUN \  
cd /usr/local/rbenv/plugins && \  
git clone git://github.com/ianheggie/rbenv-binstubs.git  
  
# Install multiple versions of ruby  
ENV CONFIGURE_OPTS --disable-install-doc  
ADD ./versions.txt /usr/local/rbenv/versions.txt  
RUN \  
echo 'gem: --no-rdoc --no-ri' >> /.gemrc && \  
xargs -L 1 rbenv install < /usr/local/rbenv/versions.txt  
  

