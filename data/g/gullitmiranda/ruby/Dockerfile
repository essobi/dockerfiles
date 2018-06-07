# The container includes:  
#  
# azukiapp/ruby:  
# * MRI Ruby 2.1.2  
# * Bundler  
# * Image Magick  
#  
FROM azukiapp/node  
MAINTAINER Azuki <support@azukiapp.com>  
  
ENV RUBY_MAJOR 2.1  
ENV RUBY_VERSION 2.1.2  
# Set $PATH so that non-login shells will see the Ruby binaries  
ENV PATH $PATH:/opt/rubies/ruby-$RUBY_VERSION/bin  
  
# Install MRI Ruby $RUBY_VERSION  
RUN curl -O http://ftp.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz && \  
tar -zxvf ruby-$RUBY_VERSION.tar.gz && \  
cd ruby-$RUBY_VERSION && \  
./configure --disable-install-doc && \  
make && \  
make install && \  
cd .. && \  
rm -r ruby-$RUBY_VERSION ruby-$RUBY_VERSION.tar.gz && \  
echo 'gem: --no-document' > /usr/local/etc/gemrc  
  
#
==============================================================================  
# Rubygems and Bundler  
#
==============================================================================  
ENV RUBYGEMS_MAJOR 2.3  
ENV RUBYGEMS_VERSION 2.3.0  
# Install rubygems and bundler  
ADD http://production.cf.rubygems.org/rubygems/rubygems-$RUBYGEMS_VERSION.tgz
/tmp/  
RUN cd /tmp && \  
tar -zxf /tmp/rubygems-$RUBYGEMS_VERSION.tgz && \  
cd /tmp/rubygems-$RUBYGEMS_VERSION && \  
ruby setup.rb && \  
/bin/bash -l -c 'gem install bundler --no-rdoc --no-ri' && \  
echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
  
# Define working directory  
WORKDIR /app  
  
# Set bash as a default process  
CMD ["bash"]  

