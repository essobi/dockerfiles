FROM ontouchstart/ruby:docker-2_2_0  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
ADD . /rails  
RUN gem install sdoc bundler  
RUN cd /rails && rake install  
RUN rails -v  
ENV HOME /home  
WORKDIR /home  

