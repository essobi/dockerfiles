FROM centos:centos6  
MAINTAINER Sparkle <popeast@gmail.com>  
  
ENV RUBY_VERSION 2.2.0  
RUN yum groupinstall -y "Development Tools"  
RUN yum install -y tar libffi-devel zlib-devel openssl-devel  
  
RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv  
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_profile  
RUN echo 'eval "$(rbenv init -)"' >> ~/.bash_profile  
RUN git clone https://github.com/sstephenson/ruby-build.git
~/.rbenv/plugins/ruby-build  
  
RUN source ~/.bash_profile && rbenv install ${RUBY_VERSION}  
RUN source ~/.bash_profile && rbenv global ${RUBY_VERSION}  
  

