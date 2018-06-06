# Using base image from official ruby docker hub  
FROM ruby:2.2.6  
# Install essential linux packages  
RUN apt-get update -qq && apt-get install -y --no-install-recommends \  
build-essential \  
libpq-dev \  
nodejs \  
npm \  
postgresql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
# Define where the application will live inside the image  
ENV RAILS_ROOT /var/www/app  
  
# Create application home. App server will need the pids dir  
RUN mkdir -p $RAILS_ROOT/tmp/pids  
  
# Set our working directory inside the image  
WORKDIR $RAILS_ROOT  
  
# Prevent bundler warnings; Ensure bundler version is >= that which created
Gemfile.lock  
RUN gem install bundler  
  
# Use the Gemfiles as Docker cache markers. Always bundle before copying app
src.  
COPY Gemfile Gemfile  
  
COPY Gemfile.lock Gemfile.lock  
  
# Finish establishing our Ruby enviornment  
RUN bundle install --deployment --without development test  
  
# Copy the CASinoApp into image  
COPY . .  
  
# Compile assets  
RUN bundle exec rake assets:precompile RAILS_ENV=production  
  
CMD ["config/containers/app_cmd.sh"]  
  

