# Base  
FROM ruby:2.2.2  
# Packages  
RUN apt-get update -qq && apt-get install -y build-essential  
# Database uses SQLite3  
RUN apt-get -y install sqlite libsqlite3-dev  
# To parse t2flows:  
RUN apt-get install -y libxml2-dev libxslt1-dev  
# To generate t2flow images  
RUN apt-get install -y libtool libmagickwand-dev graphviz ImageMagick
ghostscript  
RUN apt-get install -y nodejs  
  
# Environment  
ADD . /taverna-player-portal  
WORKDIR /taverna-player-portal  
ENV RAILS_ENV production  
## Assume Taverna server linked as "taverna"  
ENV TAVERNA_SERVER_URL http://taverna:8080  
ENV TAVERNA_SERVER_USERNAME taverna  
ENV TAVERNA_SERVER_PASSWORD taverna  
ENV RAILS_SERVE_STATIC_FILES true  
  
# Gems  
RUN bundle install  
  
# DB  
RUN bundle exec rake db:setup  
# Migrate, incase we are using a pre-existing, but outdated database  
RUN bundle exec rake db:migrate  
  
# Config  
RUN cp config/initializers/secret_token.rb.example
config/initializers/secret_token.rb  
RUN cp config/settings.yml.example config/settings.yml  
RUN cp config/initializers/taverna_server.rb.example
config/initializers/taverna_server.rb  
  
# Assets (CSS/JS)  
RUN bundle exec rake assets:precompile  
  
# Network  
EXPOSE 3000  
# Runtime  
ENTRYPOINT ["/taverna-player-portal/docker/entrypoint.sh"]  
  
# Shared  
VOLUME ["/taverna-player-portal/db/sqlite", "/taverna-player-
portal/public/system", "/taverna-player-portal/config", "/taverna-player-
portal/log"]  
  
CMD ["rails", "server", "-b", "0.0.0.0"]  
  

