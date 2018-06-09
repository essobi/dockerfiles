FROM instedd/nginx-rails:2.2  
# Install gem bundle  
ADD Gemfile /app/  
ADD Gemfile.lock /app/  
RUN bundle install --jobs 3 --deployment --without development test  
  
# Default environment settings  
ENV PUMA_OPTIONS "--preload -w 4"  
# Install the application  
ADD . /app  
  
# Generate version file  
RUN if [ -d .git ]; then git describe --always > VERSION; fi  
  
# Precompile assets  
RUN bundle exec rake assets:precompile RAILS_ENV=production
SECRET_KEY_BASE=secret  
  
# Add config files  
ADD docker/runit-web-run /etc/service/web/run  
ADD docker/database.yml /app/config/database.yml  
ADD docker/nginx-app.conf /etc/nginx/sites-enabled/app.conf  

