FROM phusion/passenger-ruby24  
MAINTAINER MarsBased "hola@marsbased.com"  
ENV HOME /home/app/decidim-vilanova  
  
# Install software dependencies  
RUN apt-get update  
RUN apt-get install -y imagemagick gettext-base  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Expose Nginx HTTP service  
EXPOSE 80  
EXPOSE 443  
# Start Nginx / Passenger  
RUN rm -f /etc/service/nginx/down  
  
# Remove the default site  
RUN rm /etc/nginx/sites-enabled/default  
  
# Create app home dir  
RUN mkdir -p $HOME  
WORKDIR $HOME  
  
# Install bundle of gems  
ADD Gemfile Gemfile  
ADD Gemfile.lock Gemfile.lock  
RUN bundle install --without development test  
  
# Add the nginx site and config  
ADD docker/nginx.conf /etc/nginx/sites-enabled/decidim-vilanova.conf  
ADD docker/rails-env.conf /etc/nginx/main.d/rails-env.conf  
  
# Add the Rails app  
ADD . /home/app/decidim-vilanova  
  
RUN RAILS_ENV=production SECRET_KEY_BASE=NOT-IMPORTANT bin/rake
assets:precompile  
  
# Add a tmp folder for pids  
RUN mkdir -p tmp/pids  
  
# Define volumes  
VOLUME $HOME/public/uploads  
VOLUME $HOME/log  
  
# Configure init scripts  
RUN mkdir -p /etc/my_init.d  
ADD docker/fix_permissions.sh /etc/my_init.d/fix_permissions.sh  
ADD docker/replace_nginx_variables.sh
/etc/my_init.d/replace_nginx_variables.sh  
ADD docker/sidekiq.sh /etc/my_init.d/sidekiq.sh  
RUN chmod +x /etc/my_init.d/*.sh  
  
RUN chown -R app:app $HOME  
  
# Clean up APT and bundler when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*.  

