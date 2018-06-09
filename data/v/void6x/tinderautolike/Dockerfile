FROM ruby:2.1  
RUN mkdir /usr/app  
WORKDIR /usr/app  
  
COPY Gemfile /usr/app/  
RUN bundle install  
  
COPY TinderAutoLike.rb /usr/app  
  
CMD ["ruby","/usr/app/TinderAutoLike.rb"]  

