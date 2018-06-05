FROM phusion/passenger-ruby23  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
  
# Add additional packages  
RUN apt-get update && apt-get install -y -o Dpkg::Options::="--force-confold"
netcat  
  
# Enable Nginx and Passenger  
RUN rm -f /etc/service/nginx/down  
  
# Add virtual host entry for the applicaiton  
RUN rm /etc/nginx/sites-enabled/default  
ADD webapp.conf /etc/nginx/sites-enabled/webapp.conf  
  
# Add environment variables in case we need them  
ADD rails-env.conf /etc/nginx/main.d/rails-env.conf  
  
# Install gems  
ADD Gemfile /tmp/  
ADD Gemfile.lock /tmp/  
WORKDIR /tmp  
RUN bundle install  
  
# Copy application into the container and use right permissions  
COPY . /home/app/cats  
RUN usermod -u 1000 app  
RUN chown -R app:app /home/app/cats  
WORKDIR /home/app/cats  
  
# Clean up APT when done  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
EXPOSE 80  

