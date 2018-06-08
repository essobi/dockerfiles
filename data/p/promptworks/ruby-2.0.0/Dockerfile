FROM centos  
MAINTAINER PromptWorks <team@promptworks.com>  
  
ADD install_ruby.sh /tmp/  
RUN /tmp/install_ruby.sh  
  
RUN gem update --system --no-document  
RUN gem install bundler --no-ri --no-rdoc  

