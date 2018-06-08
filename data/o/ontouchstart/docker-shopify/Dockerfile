FROM ontouchstart/rails:docker-4.2.0  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
ADD /home/app/Gemfile /Gemfile  
ADD /home/app/Gemfile.lock /Gemfile.lock  
RUN cd / && bundle install  
ENV HOME /home  
WORKDIR /home  

