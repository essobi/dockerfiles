FROM phusion/passenger-ruby22:0.9.18  
MAINTAINER James Pasteur "pogopolice@gmail.com"  
# Set correct environment variables.  
ENV HOME /root  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Expose Nginx HTTP service  
EXPOSE 3000  
# Start Nginx / Passenger  
RUN rm -f /etc/service/nginx/down  
  
# Remove the default site  
RUN rm /etc/nginx/sites-enabled/default  
  
# Add the nginx site and config  
ADD nginx.conf /etc/nginx/sites-enabled/webapp.conf  
ADD rails-env.conf /etc/nginx/main.d/rails-env.conf  
  
# Install bundle of gems  
WORKDIR /tmp  
ADD Gemfile /tmp/  
ADD Gemfile.lock /tmp/  
RUN gem install bundler && bundle install --jobs 20 --retry 5  
#RUN bundle install  
# Add the Rails app  
ADD . /home/app/webapp  
RUN chown -R app:app /home/app/webapp  
  
# Clean up APT and bundler when done.  
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]  

