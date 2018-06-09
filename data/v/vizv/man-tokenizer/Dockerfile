FROM ruby:2.4.1  
COPY Gemfile Gemfile.lock /app/  
WORKDIR /app  
RUN bundle install  
  
COPY . /app/  
RUN racc -o man.rb man.y  
  
EXPOSE 3000  
CMD ["ruby", "server.rb"]  

