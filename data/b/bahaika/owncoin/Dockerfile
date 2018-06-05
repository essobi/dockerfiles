FROM ubuntu:15.10  
MAINTAINER Jeremy SEBAN <jeremy@seban.eu>  
  
# Adding bitcoin repo  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8842ce5e && \  
echo "deb http://ppa.launchpad.net/bitcoin/bitcoin/ubuntu wily main" >
/etc/apt/sources.list.d/bitcoin.list  
  
# Installing required dependencies  
RUN apt-get update && \  
apt-get install -y bitcoind nginx nodejs ruby ruby-dev build-essential libxml2
libxml2-dev zlib1g-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configuring Rails application  
ENV APP_HOME /srv/app  
ENV RAILS_ENV production  
  
# Copying nginx configuration  
RUN rm -rf /etc/nginx/sites-* /etc/nginx/conf.d  
COPY ./config/dockerized/nginx.conf /etc/nginx/nginx.conf  
  
# Creating application folder  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
  
# Adding gems dependencies  
ADD ./Gemfile* $APP_HOME/  
RUN echo "gem: --no-rdoc --no-ri" > ~/.gemrc  
RUN gem install bundler && bundle install --without development  
  
# Expose HTTP port  
EXPOSE 80 8333  
# Set entrypoint  
# The entrypoint will :  
# - Starts bitcoin daemon  
# - Starts the puma server of the backend of the app  
# - Starts the nginx server in frontend  
COPY ./config/dockerized/entrypoint.rb /entrypoint  
ENTRYPOINT ["/entrypoint"]  
RUN chmod +x /entrypoint  
RUN mkdir -p /data  
  
VOLUME ["/data"]  
  
# Copying application  
ADD . $APP_HOME  
  
# Precompile assets  
RUN bundle exec rake assets:precompile  

