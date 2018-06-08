FROM bradrydzewski/base  
  
WORKDIR /home/ubuntu  
USER ubuntu  
ADD rbenv.sh /etc/drone.d/  
  
RUN export PATH=$PATH:/home/ubuntu/.rbenv/bin && \  
cd ~/.rbenv/plugins/ruby-build && \  
git pull && \  
export RBENV_VERSION=2.2.1 && \  
eval "$(rbenv init -)" && \  
CC=gcc rbenv install 2.2.1 && \  
rbenv rehash && \  
rbenv global 2.2.1 && \  
rbenv rehash && \  
gem install bundler && \  
rbenv rehash  

