FROM ruby:2.2.3  
RUN gem install bundler  
COPY . /app  
WORKDIR /app  
COPY Gemfile /app/Gemfile  
COPY app.rb /app/app.rb  
EXPOSE 4567  
RUN bundler  
CMD ["bundle", "exec", "ruby", "./app.rb"]  

