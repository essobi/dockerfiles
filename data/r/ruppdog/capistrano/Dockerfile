FROM centos:centos6  
  
# Update and Install Dependencies  
RUN \  
yum update -y && \  
yum groupinstall -y "Development Tools" && \  
yum install -y \  
wget \  
tar \  
gcc \  
automake \  
autoconf \  
curl-devel \  
openssl-devel \  
zlib-devel \  
httpd-devel \  
apr-devel \  
apr-util-devel \  
sqlite-devel \  
libtool \  
libxml2 \  
libxml2-devel \  
libxslt \  
libxslt-devel  
  
# Install Ruby 2.1.5  
RUN \  
cd /root && wget 'http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.5.tar.gz'
&& \  
tar -zxvf ruby-2.1.5.tar.gz && rm ruby-2.1.5.tar.gz && \  
cd ruby-2.1.5 && \  
./configure && make && make install  
  
# Install Ruby Gems 2.4.5  
RUN \  
cd /root && wget
'http://production.cf.rubygems.org/rubygems/rubygems-2.4.5.tgz' && \  
tar xvzf rubygems-2.4.5.tgz && rm rubygems-2.4.5.tgz && \  
cd rubygems-2.4.5 && \  
ruby setup.rb  
  
# Update Gems  
RUN gem update  
  
# Install Bundler  
RUN gem install --no-ri --no-rdoc bundler  
  
# Install Capistrano  
RUN gem install --no-ri --no-rdoc capistrano -v 3.3.5  
  

