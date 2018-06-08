FROM centos:centos5  
MAINTAINER ryan.walker@rackspace.com  
# Original author: Derek Olsen in https://github.com/someword/omnibus-centos  
# RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN yum install -y wget  
RUN wget http://download.fedoraproject.org/pub/epel/5/x86_64/epel-
release-5-4.noarch.rpm && \  
rpm -Uvh epel-release-5-4.noarch.rpm  
RUN yum groupinstall -y 'Development Tools'  
  
RUN yum install -y \  
libyaml-devel \  
libffi-devel \  
openssl-devel \  
iconv-devel \  
fakeroot \  
tar \  
openssl-devel \  
expat-devel \  
perl-ExtUtils-MakeMaker \  
curl-devel \  
golang \  
gcc44 \  
gcc44-c++ \  
python26 \  
python26-devel \  
wget  
  
# Ruby  
RUN cd /usr/src && \  
wget http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.3-p194.tar.gz && \  
tar xvzf ruby-1.9.3-p194.tar.gz && \  
cd ruby-1.9.3-p194 && \  
./configure && \  
make && \  
make install  
  
ENV CC gcc44  
ENV CXX g++44  
# RubyGems  
RUN cd /usr/src && \  
wget http://production.cf.rubygems.org/rubygems/rubygems-1.8.24.tgz && \  
tar xvzf rubygems-1.8.24.tgz && \  
cd rubygems-1.8.24 && \  
ruby setup.rb  
  
# Work around git/go version issues on centos -
https://twitter.com/gniemeyer/status/472318780472045568  
RUN yum remove -y git  
RUN yum clean all  
  
RUN cd /usr/src && \  
curl -o git-1.9.4.tar.gz
https://www.kernel.org/pub/software/scm/git/git-1.9.4.tar.gz && \  
tar xzf git-1.9.4.tar.gz && cd git-1.9.4 && \  
make prefix=/usr all && make prefix=/usr install  
  
RUN git config --global url."https://".insteadOf git://  
RUN git config --global user.email ryan.walker@rackspace.com  
RUN git config --global user.name "Ryan Walker"  
  
WORKDIR /  
  
RUN gem install bundler --no-rdoc --no-ri  
RUN /bin/bash -l -c "git clone https://github.com/ryandub/omnibus-ohai-
solo.git && cd omnibus-ohai-solo && bundle install --binstubs"  
  
# Install setuptools and virtualenv since they are no longer in EPEL for
CentOS 5  
WORKDIR /tmp  
RUN wget --no-check-certificate
http://pypi.python.org/packages/2.6/s/setuptools/setuptools-0.6c9-py2.6.egg#md5=ca37b1ff16fa2ede6e19383e7b59245a  
RUN sh setuptools-0.6c9-py2.6.egg && rm -f setuptools-0.6c9-py2.6.egg  
RUN easy_install virtualenv  
  
WORKDIR /omnibus-ohai-solo  
RUN virtualenv-2.6 venv  
ENV VIRTUAL_ENV /omnibus-ohai-solo/venv  
ENV PATH /omnibus-ohai-solo/venv/bin:$PATH  

