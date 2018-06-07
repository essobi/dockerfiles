FROM ruby:2.2.7  
ADD . /rails/ie-ccda-endpoint  
  
WORKDIR /rails/ie-ccda-endpoint  
RUN bundle install  
RUN rake db:migrate  
  
EXPOSE 3000  
CMD ["rails", "server", "-b", "0.0.0.0"]  

