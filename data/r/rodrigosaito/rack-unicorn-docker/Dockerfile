FROM rodrigosaito/ruby:2.1.2  
MAINTAINER Rodrigo Saito <rodrigo.saito@gmail.com>  
  
ADD . /app/  
  
WORKDIR /app/  
  
RUN bundle install --deployment --without development test \--jobs 4  
  
ENV RACK_ENV development  
  
CMD bundle exec unicorn -E $RACK_ENV  
  
EXPOSE 8080  

