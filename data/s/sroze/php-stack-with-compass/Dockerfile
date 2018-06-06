FROM sroze/php-stack  
  
RUN apt-get update && \  
apt-get -yq install ruby ruby-dev rubygems-integration && \  
gem install compass && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN gem install --no-rdoc --no-ri compass  
  

