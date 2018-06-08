FROM rails:onbuild  
RUN mkdir /fabrikmaps  
WORKDIR /fabrikmaps  
ADD Gemfile /fabrikmaps/Gemfile  
ADD Gemfile.lock /fabrikmaps/Gemfile.lock  
ADD . /fabrikmaps  
ENV RAILS_ENV production  
ENV RACK_ENV production  
RUN bundle install  
RUN rake db:migrate  
RUN rake db:seed  
RUN apt-get update  

