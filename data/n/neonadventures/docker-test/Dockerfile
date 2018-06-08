FROM ruby:2.1  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ADD Gemfile /usr/src/app/  
ADD Gemfile.lock /usr/src/app/  
RUN bundle install --system  
  
ADD . /usr/src/app  
  
EXPOSE 4567  
CMD ["ruby", "app.rb", "-o", "0.0.0.0"]

