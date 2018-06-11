FROM ruby:2.3.1  
MAINTAINER borisding@zhulux.com  
ENV BUNDLER_VERSION 1.12.5  
ENV RAILS_VERSION 5.0.0.1  
RUN apt-get update && \  
apt-get install postgresql-client graphicsmagick imagemagick ghostscript
libpq-dev libmysqlclient-dev libgs-dev -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN gem install bundler --version "$BUNDLER_VERSION" && \  
gem install rails --version "$RAILS_VERSION"  
  
CMD [ "pry" ]  

