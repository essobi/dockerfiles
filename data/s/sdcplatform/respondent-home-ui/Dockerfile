FROM ruby:2.5  
WORKDIR /respondent_home_ui  
COPY . /respondent_home_ui  
  
RUN bundle install  
  
ENV PORT 9292  
EXPOSE $PORT  
CMD ["sh", "-c", "bundle exec rackup config.ru --host 0.0.0.0 --port ${PORT}"]  

