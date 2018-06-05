FROM ruby:2.2  
RUN apt-get update -qq  
RUN apt-get install -y libpq-dev libxml2-dev libxslt1-dev nodejs  
  
COPY . /srv/blog.lamarmite.ca  
WORKDIR /srv/blog.lamarmite.ca  
  
ENV RAILS_ENV production  
  
RUN bundle install --deployment  
RUN bundle exec rake assets:precompile  
  
EXPOSE 3000  

