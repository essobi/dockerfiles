FROM ontouchstart/ruby:docker-2_2_0  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
ADD . /pry  
RUN cd /pry && rake install  
RUN pry -v  
ENV HOME /home  
WORKDIR /home  

