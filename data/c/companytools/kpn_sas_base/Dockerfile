FROM centos:6.6  
MAINTAINER docker@companytools.nl  
  
RUN yum -y groupinstall "Development Tools"  
RUN yum -y install libxml2-devel libxslt-devel libyaml-devel openssl-devel
readline-devel gdbm-devel libffi-devel  
RUN yum -y install wget tar git  
RUN yum -y install libtool libxml2 libxslt libyaml openssl readline unzip zip
zlib dos2unix  
  
ENV RUBY_MAJOR 2.1  
ENV RUBY_MINOR 8  
ENV RUBY_VERSION $RUBY_MAJOR.$RUBY_MINOR  
RUN cd /tmp \  
&& wget http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz \  
&& tar xvfvz ruby-$RUBY_VERSION.tar.gz \  
&& cd ruby-$RUBY_VERSION \  
&& ./configure \  
&& make \  
&& make install  
  
RUN gem update --system \  
&& gem install bundler \  
&& gem update  
  
RUN rm -rf /tmp/ruby-$RUBY_VERSION \  
&& rm -rf /tmp/ruby-$RUBY_VERSION.tar.gz  
  
RUN echo "gem: --no-document" > /etc/gemrc  

