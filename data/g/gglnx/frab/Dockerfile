# Using the base image with Ruby 2.0 from Phusion  
# See: https://github.com/phusion/passenger-docker  
FROM phusion/passenger-ruby22:0.9.18  
# Set maintainer  
MAINTAINER Dennis Morhardt "info@dennismorhardt.de"  
# Set correct environment variables.  
ENV HOME /home/app  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
  
# Update OS  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
# Start Nginx / Passenger  
RUN rm -f /etc/service/nginx/down  
  
# Remove the default site  
RUN rm /etc/nginx/sites-enabled/default  
  
# Add the nginx configuration  
ADD nginx.conf /etc/nginx/sites-enabled/frab.conf  
  
# Install dependencies  
RUN apt-get install -y nodejs imagemagick  
  
# Clone frab from GitHub  
WORKDIR /home/app/frab  
RUN git clone https://github.com/frab/frab.git .  
RUN git pull && git checkout 1f67274209cf6b55e0a505a8fb3bfcd761e93d6b  
RUN chown -R app:app /home/app/frab  
  
# Install gem dependencies  
RUN sudo -u app bundle install --deployment --without=pg sqlite3  
  
# Setup persistent storage  
RUN rm -rf public/system  
VOLUME /home/app/shared  
  
# Setup init script  
RUN mkdir -p /etc/my_init.d  
ADD init.sh /etc/my_init.d/99_frab.sh  
RUN chmod +x /etc/my_init.d/99_frab.sh  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Expose port  
EXPOSE 80  

