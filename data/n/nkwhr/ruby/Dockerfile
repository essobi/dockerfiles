FROM centos:centos6  
  
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm && \  
yum -y update && \  
yum -y groupinstall "Development Tools" && \  
yum -y install zlib-devel openssl-devel readline-devel ncurses-devel libffi-
devel libxml2-devel libxslt-devel libcurl-devel libicu-devel libyaml-devel &&
\  
yum clean all  
  
RUN curl --progress http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz
| tar xz && \  
cd ruby-2.1.2 && \  
./configure --disable-install-doc && \  
make -j2 && make install && \  
cd .. && rm -rf ruby-2.1.2*  
  
RUN echo 'gem: --no-rdoc --no-ri' > ~/.gemrc && \  
gem update \--system && \  
gem install bundler  
  

