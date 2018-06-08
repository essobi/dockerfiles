# Using instructions from https://github.com/phusion/passenger-docker  
# Use phusion/passenger-full as base image. To make your builds reproducible,
make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/passenger-docker/blob/master/Changelog.md for  
# a list of version numbers.  
# OR live on the wild side and use latest  
FROM phusion/passenger-ruby23  
MAINTAINER David Parrish <daveparrish@tutanota.com>  
  
# Set correct environment variables.  
ENV HOME /root  
  
# COPY default redmine to build default gems  
COPY redmine /home/app/redmine  
COPY redmine/config/database.yml.example /home/app/redmine/config/database.yml  
  
# Get/build redmine requirements  
# apt-get: nokogirl, rmagick, mysql  
# Build gems  
# Clean up apt  
# Enable nginx  
# Increase client_max_body_size to 20m in nginx.conf  
RUN apt-get update && \  
apt-get -y --no-install-recommends install \  
libxslt1-dev libxml2-dev imagemagick libmagickwand-dev libmysqlclient-dev
tzdata && \  
apt-get clean && \  
cd /home/app/redmine && bundle install --without development test && \  
rm -r /var/lib/apt/lists/* && \  
rm -f /etc/service/nginx/down && \  
echo "# Managed by Dockerfile\n\nclient_max_body_size 20m;" >
/etc/nginx/conf.d/client_max_body_size.conf  

