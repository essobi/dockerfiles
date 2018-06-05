FROM phusion/passenger-ruby22:0.9.15  
# Set correct environment variables.  
ENV HOME /root  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
  
# Expose port 80 for nginx and 3000 for rails in dev mode  
EXPOSE 80 3000  
# Start Nginx / Passenger  
RUN rm -f /etc/service/nginx/down  
  
# Run Bundle in a cache efficient way  
ADD Gemfile /tmp/Gemfile  
ADD Gemfile.lock /tmp/Gemfile.lock  
# TODO: what about sudo -u app bundle install --deployment?  
# See: https://intercityup.com/blog/deploy-rails-app-including-database-
configuration-env-vars-assets-using-docker.html  
RUN cd /tmp && bundle install  
  
# Remove the default site and replace it with our site  
RUN rm /etc/nginx/sites-enabled/default  
ADD config/nginx/webapp.conf /etc/nginx/sites-enabled/webapp.conf  
ADD config/nginx/rails-env.conf /etc/nginx/main.d/rails-env.conf  
  
# Add the dev startup script  
RUN mkdir -p /etc/my_init.d/  
ADD run-dev.sh /etc/my_init.d/  
  
# Add source code  
RUN mkdir -p /home/app/webapp/  
WORKDIR /home/app/webapp/  
ADD . /home/app/webapp/  
RUN chown -R app:app /home/app/webapp/  
RUN sudo -u app RAILS_ENV=production rake assets:precompile  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

