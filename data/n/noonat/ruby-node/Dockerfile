FROM noonat/rbenv-nodenv  
MAINTAINER Nathan Ostgard <noonat@phuce.com>  
  
ENV RUBY_VERSION=2.2.2 NODE_VERSION=0.12.7  
RUN rbenv install $RUBY_VERSION && \  
CONFIGURE_OPTS="--disable-install-doc" rbenv global $RUBY_VERSION && \  
gem install bundler  
  
RUN nodenv install $NODE_VERSION && \  
nodenv global $NODE_VERSION && \  
nodenv rehash  
  
CMD ["/bin/bash"]  

