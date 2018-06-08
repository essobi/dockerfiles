FROM keboola/base  
MAINTAINER Slowpath Team <support@slowpath.com>  
  
ENV RUBY_DIR /ruby/  
ENV RUBY_VERSION 2.1.5  
ENV RUBY_INSTALL $RUBY_DIR/$RUBY_VERSION  
  
# Get the system ready  
RUN yum update -y  
RUN yum install -y gcc-c++ which wget tar git \  
patch readline readline-devel zlib zlib-devel \  
libyaml-devel libffi-devel libxml-devel \  
openssl-devel make bzip2 autoconf automake libtool bison  
  
# Install ruby  
RUN mkdir $RUBY_DIR && \  
cd $RUBY_DIR && \  
git clone https://github.com/sstephenson/ruby-build.git && \  
$RUBY_DIR/ruby-build/install.sh && \  
cd $RUBY_DIR/ruby-build && ./bin/ruby-build $RUBY_VERSION $RUBY_INSTALL && \  
rm -rf $RUBY_DIR/ruby-build  
  
ENV PATH $RUBY_INSTALL/bin:$PATH  
  
# Skip installing gem documentation  
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"  
  
# Install things globally, for great justice  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
RUN gem install bundler \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin"  
  
# Don't create ".bundle" in all our apps  
ENV BUNDLE_APP_CONFIG $GEM_HOME  

