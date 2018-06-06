FROM ruby:2.3.5  
RUN apt-get update && apt-get install -y cron nodejs  
RUN mkdir app  
WORKDIR app  
  
COPY Gemfile ./Gemfile  
COPY Gemfile.lock ./Gemfile.lock  
  
RUN bundle install -j 20  
COPY . .  
CMD cron && bundle exec whenever --update-crontab && bundle exec rails s -b
0.0.0.0  

