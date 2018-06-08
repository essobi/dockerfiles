FROM centos:6  
MAINTAINER neko-neko  
ENV RUBY_VERSION 2.3.0  
RUN yum -y update && yum -y install \  
autoconf \  
automake \  
bison \  
curl-devel \  
gcc \  
gcc-c++ \  
git-core \  
httpd-devel \  
libevent-devel \  
libxml2 \  
libxml2-devel \  
mysql-devel \  
openssl \  
openssl-devel \  
readline-devel \  
sqlite-devel \  
zlib \  
zlib-devel \  
libxslt \  
libxslt-devel \  
wget \  
&& yum clean all  
  
# Ruby install  
RUN wget --no-check-certificate https://cache.ruby-
lang.org/pub/ruby/2.3/ruby-$RUBY_VERSION.tar.gz && tar -xzvf
ruby-$RUBY_VERSION.tar.gz  
WORKDIR ruby-$RUBY_VERSION  
RUN ./configure && make && make install  
WORKDIR /  
  
# Bundler install  
RUN gem install bundler --no-document  
  
CMD ["/bin/bash"]  

