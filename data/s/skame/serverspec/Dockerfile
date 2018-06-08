FROM ruby:2.4-alpine  
  
RUN mkdir /serverspec  
WORKDIR /serverspec  
ADD Gemfile /serverspec/  
RUN bundle  
  
CMD /bin/bash  

