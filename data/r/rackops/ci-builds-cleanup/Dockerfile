FROM ruby:2.1  
COPY Gemfile /usr/src/app/  
WORKDIR /usr/src/app/  
RUN bundle install  
COPY . /usr/src/app/  
CMD ["clockwork", "./clockwork.rb"]  

