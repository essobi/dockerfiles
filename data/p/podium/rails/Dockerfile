FROM phusion/passenger-ruby23:0.9.24  
# Set correct environment variables for passenger  
ENV HOME /root  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
  
# Update OS  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Enable phusion and nginx  
RUN rm -f /etc/service/nginx/down  
RUN rm /etc/nginx/sites-enabled/default  
COPY nginx/app.conf /etc/nginx/sites-enabled/app.conf  
  
# Whitelist environment variables  
# COPY nginx/env.conf /etc/nginx/main.d/env.conf  

