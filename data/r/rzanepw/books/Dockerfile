FROM ruby:2.3.3-slim  
ENV RAILS_ENV=production  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev  
RUN mkdir /app  
WORKDIR /app  
COPY Gemfile /app/Gemfile  
COPY Gemfile.lock /app/Gemfile.lock  
RUN bundle install  
COPY . /app  
RUN rake assets:precompile  
  
EXPOSE 3000  
CMD ["/app/bin/run"]  

