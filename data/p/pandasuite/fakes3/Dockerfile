#  
# Fakes3 Dockerfile  
#  
# https://github.com/beingenious/docker-fakes3.git  
#  
# Pull base image.  
FROM ruby:2-alpine  
  
# Install fakes3 with dependancies  
RUN apk --update add --virtual build-dependencies git && \  
gem install --no-ri --no-rdoc specific_install && \  
gem specific_install -l https://github.com/benjaminbarbe/fake-s3.git && \  
apk del build-dependencies  
  
# Attach volumes.  
VOLUME /var/data/fakes3  
  
# Set working directory.  
WORKDIR /var/data/fakes3  
  
# Expose ports.  
EXPOSE 80  

