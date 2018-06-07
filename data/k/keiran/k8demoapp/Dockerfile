FROM ruby:2.3.0  
ADD . /code  
WORKDIR /code  
RUN bundle install  
EXPOSE 4567  
CMD ["ruby", "/code/api.rb"]  

