FROM ruby:2.2.3  
RUN apt-get update -qq && apt-get install -y build-essential vim  
  
# postgres client  
RUN apt-get install -y libpq-dev  
  
RUN mkdir /srv/kanban-server  
WORKDIR /srv/kanban-server  
  
ADD Gemfile* /srv/kanban-server/  
  
# --- Add this to your Dockerfile ---  
ENV BUNDLE_GEMFILE=/srv/kanban-server/Gemfile \  
BUNDLE_JOBS=2 \  
BUNDLE_PATH=/bundle  
  
RUN bundle install  
RUN gem install rerun  
RUN bundle exec gem install bundler  
  
ADD . /srv/kanban-server  
WORKDIR /srv/kanban-server  
  
CMD ["rackup"]

