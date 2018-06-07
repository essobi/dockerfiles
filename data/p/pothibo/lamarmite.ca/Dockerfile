FROM ruby:2.2  
RUN apt-get update -qq  
RUN apt-get install -y libpq-dev libxml2-dev libxslt1-dev nodejs  
  
COPY . /srv/lamarmite.ca  
WORKDIR /srv/lamarmite.ca  
  
ENV RAILS_ENV production  
  
RUN bundle install --deployment  
  
EXPOSE 3000  

