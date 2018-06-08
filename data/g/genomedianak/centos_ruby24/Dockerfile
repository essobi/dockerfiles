FROM centos:7  
  
RUN set -x && \  
yum -y install bzip2 && \  
yum -y install git && \  
yum -y install gcc && \  
yum -y install make && \  
yum -y install openssl-devel && \  
yum -y install libffi-devel && \  
yum -y install readline-devel && \  
yum -y install zlib-devel && \  
yum -y install which && \  
curl -O http://ftp.ruby-lang.org/pub/ruby/2.4/ruby-2.4.3.tar.gz && \  
tar -zxvf ruby-2.4.3.tar.gz && \  
cd ruby-2.4.3 && \  
./configure --disable-install-doc && \  
make && \  
make install && \  
cd .. && \  
rm -r ruby-2.4.3 ruby-2.4.3.tar.gz && \  
echo 'gem: --no-document' > /usr/local/etc/gemrc  
  
# Install Bundler for each version of ruby  
RUN \  
echo 'gem: --no-rdoc --no-ri' >> /.gemrc && \  
gem install bundler  

