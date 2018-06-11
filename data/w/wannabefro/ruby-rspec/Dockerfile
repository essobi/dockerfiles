# docker image for Ruby and Rspec  
# Based off http://www.activestate.com/blog/2014/01/using-docker-run-ruby-
rspec-ci-jenkins  
FROM ubuntu  
  
RUN apt-get update  
RUN apt-get -y install wget  
RUN apt-get -y install git  
  
# install Ruby 2.1.0  
RUN apt-get -y install build-essential zlib1g-dev libreadline-dev libssl-dev
libcurl4-openssl-dev  
RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
~/.rbenv/plugins/ruby-build  
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_profile  
RUN echo 'eval "$(rbenv init -)"' >> ~/.bash_profile  
ENV PATH /.rbenv/bin:/.rbenv/shims:$PATH  
RUN echo PATH=$PATH  
RUN rbenv init -  
RUN rbenv install 2.1.0 && rbenv global 2.1.0  
  
# never install a ruby gem docs  
RUN echo "gem: --no-rdoc --no-ri" >> ~/.gemrc  
  
# Install bundler and the "bundle" shim  
RUN gem install bundler && rbenv rehash  
  
RUN gem install rspec && rbenv rehash  

