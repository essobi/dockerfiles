FROM ruby:2.4-slim  
LABEL maintainer="Andrew Porter <andy@wavetronix.com>"  
RUN apt-get update -qq && apt-get install -qq -y --no-install-recommends \  
build-essential \  
git \  
imagemagick \  
libpq-dev \  
nodejs  
ENV APP_DIR /app  
RUN mkdir -p $APP_DIR  
WORKDIR $APP_DIR  
COPY Gemfile* ./  
RUN bundle install --system  
COPY . .  
# RUN bundle exec rails RAILS_ENV=production
DATABASE_URL=postgresql://user:pass@127.0.0.1/dbname
ACTION_CABLE_ALLOWED_REQUEST_ORIGINS=foo,bar SECRET_TOKEN=dummytoken
assets:precompile  
EXPOSE 3000  
VOLUME ["$APP_DIR/public"]  
CMD ["puma", "-C", "config/puma.rb"]  

