FROM ruby:2.0.0  
  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev
libsqlite3-dev qt5-default libqt5webkit5-dev ssmtp  
  
WORKDIR /tmp  
ADD Gemfile /tmp/Gemfile  
ADD Gemfile.lock /tmp/Gemfile.lock  
RUN bundle install  
  
RUN mkdir /app  
WORKDIR /app  
  
ADD app /app/app  
ADD Gemfile Gemfile  
ADD Gemfile.lock Gemfile.lock  
ADD Rakefile Guardfile config.ru /app/  
ADD bin /app/bin  
ADD config /app/config  
ADD db /app/db  
ADD features /app/features  
ADD lib /app/lib  
ADD public /app/public  
ADD script /app/script  
ADD spec /app/spec  
ADD vendor /app/vendor  
  
# Precompile assets  
COPY config/database.example.yml /app/config/database.yml  
COPY config/elasticsearch.example.yml /app/config/elasticsearch.yml  
COPY config/redis.example.yml /app/config/redis.yml  
RUN RAILS_ENV=production bundle exec rake assets:precompile --trace  
  
VOLUME ["/app/log", "/app/public/uploads", "/app/public/assets"]  
  
#CMD ["rails", "server", "-b", "0.0.0.0"]  
  
CMD ["bundle", "exec", "unicorn", "-c", "/app/config/unicorn.rb", "-p",
"3000", "-E", "production"]  

