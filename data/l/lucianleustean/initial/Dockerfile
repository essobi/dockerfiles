FROM ruby:2.3.0  
# Install and setup NGINX  
RUN \  
apt-get update && \  
apt-get install -y nginx && \  
rm -rf /var/lib/apt/lists/* && \  
chown -R www-data:www-data /var/lib/nginx  
  
# Expose ports.  
EXPOSE 80  
# Install requirements for app  
RUN apt-get update \  
&& apt-get -y install apt-utils \  
build-essential \  
git-core \  
curl wget libssl-dev \  
libreadline-dev \  
zlib1g zlib1g-dev \  
libcurl4-openssl-dev \  
libxslt-dev libxml2-dev \  
libsqlite3-dev \  
nodejs \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV APP_HOME /initial  
  
RUN mkdir $APP_HOME /bundle /bundle-cache $APP_HOME/sockets  
  
WORKDIR $APP_HOME  
  
COPY Gemfile /bundle-cache/Gemfile  
COPY Gemfile.lock /bundle-cache/Gemfile.lock  
RUN cd /bundle-cache && \  
bundle install \  
\--jobs=4 \  
\--path=/bundle-cache/.bundle \  
\--deployment \  
\--without test development  
  
COPY . $APP_HOME  
  
RUN cp -a /bundle-cache/.bundle $APP_HOME  
RUN bundle exec rake assets:precompile  
  
CMD bundle exec rails server -p 80  

