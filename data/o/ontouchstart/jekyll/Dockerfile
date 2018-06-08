FROM ontouchstart/ruby:docker-2_2_0  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
ADD . /jekyll  
RUN gem install therubyracer --no-ri --no-rdoc  
RUN cd /jekyll && rake build && gem install pkg/jekyll-2.5.3.gem --no-ri --no-
rdoc  
RUN jekyll -v  
ENV HOME /home  
WORKDIR /home  

