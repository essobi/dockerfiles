# The container includes Nginx + Passenger on top of 'nepalez/ruby':  
#  
# * Ubuntu 14.04  
# * Git  
# * MRI Ruby 2.1.2  
# * Bundler  
# * Foreman  
#  
# Adds:  
#  
# * Passenger  
# * Nginx  
#  
  
FROM nepalez/ruby  
MAINTAINER Andrew Kozin <andrew.kozin@gmail.com>  
  
# Setup Ruby  
RUN apt-get update -qq && apt-get upgrade -y -qq  
  
#
==============================================================================  
# Phusion Passenger, Nginx version  
#
==============================================================================  
  
ENV PASSENGER_VERSION 4.0.37  
  
# Install passenger  
RUN /bin/bash -l -c \  
'gem install passenger --version $PASSENGER_VERSION'  
  
# Install passenger-nginx  
RUN /bin/bash -l -c \  
'passenger-install-nginx-module --auto-download --auto --prefix=/opt/nginx'  
  
# Update system finally  
RUN apt-get update  
  
# Clean up APT and temporary files when done  
RUN apt-get clean -qq && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Define working directory.  
WORKDIR /app  
  
# Expose port for Passenger  
EXPOSE 443  

