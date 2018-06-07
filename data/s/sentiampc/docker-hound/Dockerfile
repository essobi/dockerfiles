FROM ruby:2.3.4  
RUN apt-get update \  
&& apt-get install -y apt-transport-https \  
&& curl -sS https://deb.nodesource.com/gpgkey/nodesource.gpg.key \  
| apt-key add - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg \  
| apt-key add - \  
&& echo "deb https://deb.nodesource.com/node_7.x jessie main" \  
> /etc/apt/sources.list.d/nodesource.list \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" \  
> /etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
# For assets compilation  
nodejs \  
yarn \  
# # Capybara-webkit deps  
# dbus-1-dbg \  
# libqt5webkit5-dev \  
# qt5-default \  
# xvfb \  
# # Git  
# git \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# && dbus-uuidgen > /etc/machine-id  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1  
  
RUN mkdir -p /usr/src/app  
RUN git clone https://github.com/houndci/hound /usr/src/app \  
&& cd /usr/src/app \  
&& git reset --hard 846133f272277f577239f862a2dd68a28af0cc7b  
WORKDIR /usr/src/app  
  
RUN gem install bundler \  
&& bundle install --without development test  
  
RUN yarn install --production true  
  
COPY rails-entrypoint.sh /usr/src/app/  
RUN chmod 0755 rails-entrypoint.sh  
ENTRYPOINT ["/usr/src/app/rails-entrypoint.sh"]  
CMD bundle exec rails s -b0.0.0.0  

