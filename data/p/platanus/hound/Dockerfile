FROM ruby:2.5.0  
RUN apt-get update && apt-get install -y apt-transport-https \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add node source  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
-  
RUN echo 'deb https://deb.nodesource.com/node_8.x jessie main' >
/etc/apt/sources.list.d/nodesource.list  
RUN echo 'deb-src https://deb.nodesource.com/node_8.x jessie main' >>
/etc/apt/sources.list.d/nodesource.list  
  
# Add yarn source  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo 'deb https://dl.yarnpkg.com/debian/ stable main' >
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
# For assets compilation  
nodejs \  
yarn \  
# Capybara-webkit deps  
dbus-1-dbg \  
libqt5webkit5-dev \  
qt5-default \  
xvfb \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& dbus-uuidgen > /etc/machine-id  
  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
RUN bundle install  
  
COPY package.json /usr/src/app/  
COPY yarn.lock /usr/src/app/  
RUN yarn  
  
COPY . /usr/src/app  
  
CMD bundle exec rails s -b0.0.0.0  

