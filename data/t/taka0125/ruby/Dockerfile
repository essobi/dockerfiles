FROM centos:6.8  
MAINTAINER Takahiro Ooishi <taka0125@gmail.com>  
  
RUN yum -y update && \  
yum -y install gcc git libffi-devel openssl-devel readline-devel zlib-devel
gcc-c++  
  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv && \  
git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build && \  
sh ./root/.rbenv/plugins/ruby-build/install.sh  
  
ENV PATH /root/.rbenv/bin:$PATH  
  
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> /root/.bashrc && \  
echo 'eval "$(rbenv init -)"' >> /root/.bashrc  
  
ENV CONFIGURE_OPTS --disable-install-doc  
  
ENV RUBY_VERSION 2.3.1  
RUN rbenv install $RUBY_VERSION && \  
rbenv global $RUBY_VERSION && \  
$(rbenv which gem) install bundler && \  
rbenv rehash  
  
CMD ["/bin/bash"]  

