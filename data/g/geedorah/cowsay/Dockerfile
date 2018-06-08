FROM ruby:2.2  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN bundle install  
  
CMD ["ruby","app.rb"]  

