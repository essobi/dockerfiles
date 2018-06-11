FROM ruby:2.4.1-slim  
  
# Image author/maintainer  
MAINTAINER Randy Lowe <randy@weblogix.ca>  
  
# Install tools and dependencies  
RUN apt-get update && apt-get install -y build-essential sqlite3
libsqlite3-dev  
  
# Install Mailcatcher (https://coderwall.com/p/spo6bq/default-no-ri-no-rdoc-
on-ruby-gem-installation)  
RUN gem install mailcatcher --no-ri --no-rdoc  
  
# Cleanup  
RUN apt-get remove \--purge -y build-essential libsqlite3-dev  
RUN apt-get autoclean  
RUN apt-get clean  
  
# smtp port  
EXPOSE 1025  
  
# http port  
EXPOSE 1080  
  
CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]

