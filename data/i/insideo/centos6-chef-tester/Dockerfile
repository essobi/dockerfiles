FROM insideo/centos6-java8-build  
MAINTAINER ccondit@randomcoder.com  
  
RUN \  
touch /var/lib/rpm/* && \  
yum -y install openssl-devel && \  
yum clean all && \  
mkdir -p /ruby-build && \  
cd /ruby-build && \  
curl -O http://cache.ruby-lang.org/pub/ruby/2.4/ruby-2.4.0.tar.xz && \  
tar xf ruby-2.4.0.tar.xz && \  
cd ruby-2.4.0 && \  
./configure --prefix=/usr/local \--enable-shared && \  
make -j4 && \  
make install && \  
cd / && \  
rm -rf /ruby-build  
  
RUN \  
mkdir -p /chef-rpms && \  
cd /chef-rpms && \  
curl -O
https://packages.chef.io/files/stable/chef/12.12.15/el/6/chef-12.12.15-1.el6.x86_64.rpm
&& \  
yum -y localinstall chef-12.12.15-1.el6.x86_64.rpm && \  
yum clean all && \  
cd / && \  
rm -rf /chef-rpms  
  
RUN \  
gem install --no-ri --no-rdoc berkshelf -v 5.6.2  
  
RUN \  
touch /var/lib/rpm/* && \  
yum -y install gettext perl-ExtUtils-MakeMaker expat curl-devel && \  
yum clean all && \  
mkdir -p /git-build && \  
cd /git-build && \  
curl -O https://www.kernel.org/pub/software/scm/git/git-2.11.1.tar.xz && \  
tar xf git-2.11.1.tar.xz && \  
cd git-2.11.1 && \  
./configure --prefix=/usr/local && \  
make -j4 && \  
make install && \  
cd / && \  
rm -rf /git-build  
  
RUN \  
touch /var/lib/rpm/* && \  
yum -y install openssh-clients && \  
yum clean all  
  

