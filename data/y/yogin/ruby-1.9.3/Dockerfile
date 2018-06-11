FROM yogin/rbenv  
MAINTAINER Anthony Powles  
  
# install ruby and bundler  
ENV RUBY_VERSION 1.9.3-p484  
  
RUN rbenv install ${RUBY_VERSION} \  
&& rbenv global ${RUBY_VERSION} \  
&& gem update --system \  
&& gem install bundler \  
&& rbenv rehash  
  

