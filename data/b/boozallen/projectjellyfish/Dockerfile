FROM ruby:2.3.3-slim  
  
ENV APT_PACKAGES "git gcc g++ make patch binutils libc6-dev libffi-dev libssl-
dev libyaml-dev zlib1g-dev libgmp-dev libxml2-dev libxslt1-dev libpq-dev
libreadline-dev"  
ENV APT_REMOVE_PACKAGES "anacron cron openssh-server postfix"  
RUN apt-get update \  
&& apt-get -y dist-upgrade \  
&& apt-get install -y --no-install-recommends $APT_PACKAGES \  
&& apt-get remove \--purge -y $APT_REMOVE_PACKAGES \  
&& apt-get autoremove --purge -y  
  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config \--global frozen 1  
  
# Make and switch to the app directory  
WORKDIR /app  
  
# Setup Rails  
ENV RAILS_ENV=production \  
RAILS_LOG_TO_STDOUT=1  
COPY Gemfile Gemfile.lock /app/  
COPY lib /app/lib  
RUN bundle install --deployment --jobs 4 --without development test \  
&& find vendor/bundle -name *.gem -delete  
  
COPY . /app/  
RUN mkdir -p db public/assets log tmp vendor \  
&& bundle exec rake assets:precompile SECRET_KEY_BASE=noop
DATABASE_URL=postgres://noop REDIS_URL=redis://noop  
  
VOLUME [ "/app/public" ]  

