FROM kapost/rbenv  
MAINTAINER Kapost Engineering <noreply@kapost.com>  
  
# Install ruby  
RUN rbenv install 2.2.3 && \  
rbenv global 2.2.3 && \  
echo 'gem: --no-rdoc --no-ri' >> /$HOME/.gemrc  
  
# Install Bundler for each version of ruby  
RUN gem install bundler && \  
rbenv rehash && \  
bundle --version && \  
ruby --version && \  
rbenv install 2.2.0-dev && \  
rbenv rehash  
RUN curl --silent --location https://deb.nodesource.com/setup_0.12 | bash -  
RUN apt-get install --yes nodejs  

