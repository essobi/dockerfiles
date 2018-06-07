FROM ruby:2.4.2  
ADD Gemfile /app/  
ADD Gemfile.lock /app/  
RUN apt-get update && apt-get install -y build-essential  
ADD . /app  
  
Workdir /app  
RUN bundle install  
  
  
ENV PORT 3000  
EXPOSE 3000  
CMD ["ruby", "app.rb"]  

