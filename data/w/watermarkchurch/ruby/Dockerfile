FROM watermarkchurch/base:latest  
MAINTAINER "Travis Petticrew <tpetticrew@watermark.org>"  
ENV RUBY_BUILD_URL https://github.com/sstephenson/ruby-
build/archive/v20140905.tar.gz  
ENV RUBY_BUILD_RUBY_VERSION 2.1.2  
RUN mkdir /build  
ADD . /build  
RUN /build/install.sh  
  

