FROM phusion/passenger-ruby24:0.9.27  
MAINTAINER MarsBased "hola@marsbased.com"  
ENV HOME /home/app/decidim-diba  
  
# Locales configuration  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Install software dependencies  
RUN apt-get update  
RUN apt-get install -y imagemagick gettext-base tzdata  
  
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
ADD decidim-census decidim-census  
ADD decidim-diba_census_api decidim-diba_census_api  
ADD decidim-age_action_authorization decidim-age_action_authorization  
ADD decidim-ldap decidim-ldap  
RUN bundle install --without development test  
  
# Add the nginx site and config  
ADD docker/nginx.conf /etc/nginx/sites-enabled/decidim-diba.conf  
ADD docker/rails-env.conf /etc/nginx/main.d/rails-env.conf  
  
# Add the Rails app  
ADD . /home/app/decidim-diba  
  
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
ADD docker/replace_nginx_env_variables.sh
/etc/my_init.d/replace_nginx_variables.sh  
ADD docker/sidekiq.sh /etc/my_init.d/sidekiq.sh  
RUN chmod +x /etc/my_init.d/*.sh  
  
RUN chown -R app:app $HOME  
  
# Clean up APT and bundler when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*.  

