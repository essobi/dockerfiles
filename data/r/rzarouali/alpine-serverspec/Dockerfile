FROM ruby:alpine  
  
MAINTAINER Rachid Zarouali <rzarouali@gmail.com>  
  
RUN mkdir /serverspec /project  
WORKDIR /serverspec  
ADD Gemfile /serverspec/  
RUN bundle  
  
WORKDIR /project  
  
VOLUME /project  
  
CMD /bin/bash  
  

