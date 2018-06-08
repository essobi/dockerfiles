FROM ruby:2.3.0  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
  
RUN mkdir -p /docker-test  
WORKDIR /docker-test  
  
COPY Gemfile Gemfile.lock ./  
RUN gem install bundler && bundle install --jobs 20 --retry 5  
  
COPY . ./  
  
EXPOSE 3000  
CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]  

