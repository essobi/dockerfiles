FROM ontouchstart/docker-ruby-1.9  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
ADD Gemfile ./Gemfile  
RUN bundle install  
RUN rails -v  
  
ENV HOME /home  
WORKDIR /home  

