FROM ruby:2.3.0-slim  
  
RUN echo deb http://http.debian.net/debian jessie-backports main >>
/etc/apt/sources.list.d/backports.list  
  
RUN apt-get update -qq && apt-get install -y --force-yes build-essential
libpq-dev postgresql-client nodejs imagemagick  
  
ENV RAILS_ROOT /home/deployer/web_pass_test  
  
RUN mkdir -p $RAILS_ROOT/tmp/pids  
  
WORKDIR $RAILS_ROOT  
  
COPY Gemfile Gemfile  
  
COPY Gemfile.lock Gemfile.lock  
  
RUN gem install bundler  
  
RUN bundle install --without test development  
  
COPY . .  
  
EXPOSE 3000  
CMD ["config/containers/app_cmd.sh"]  

