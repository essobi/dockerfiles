FROM ruby:2.3.3  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev vim
nodejs mysql-client  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
RUN bundle install  
  
COPY . /usr/src/app  
  
EXPOSE 3000  
CMD ["unicorn", "-c", "config/unicorn.rb"]

