FROM vouch/rbenv  
MAINTAINER Ben Yee <ben@vouch.com>  
ENV INSTALL_RUBY_VERSION 2.2.2  
RUN rbenv install $INSTALL_RUBY_VERSION  
RUN rbenv global $INSTALL_RUBY_VERSION  
RUN echo 'gem: --no-rdoc --no-ri' >> /$HOME/.gemrc  
RUN gem install bundler  
RUN rbenv rehash  

