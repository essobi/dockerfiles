FROM ruby:2.4  
MAINTAINER leifcr@gmail.com  
  
# Add https transport to apt  
RUN apt-get update -qq && apt-get install -y apt-transport-https  
  
# Install updated nodejs, yarn and build packages  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
>> /etc/apt/sources.list.d/google.list \  
&& apt-get update -qq && apt-get install -y \  
build-essential \  
libpq-dev \  
default-libmysqlclient-dev \  
libxml2-dev \  
libxslt1-dev \  
mysql-client \  
wget \  
nodejs \  
yarn \  
&& apt-get install -y google-chrome-stable --no-install-recommends  
  
# For staging and production env, duck-cli must be installed to be able to
download refile assets  
ENV APP_HOME /app  
  
# If encoding errors occur, adjust locale.  
ENV LANG C.UTF-8  
# Phantomjs installation  
ENV PHANTOMJS_VERSION 2.1.1  
# Bitbucket dl (usually has issues)  
# Install phantomjs for testing purposes (only used on guard), but easier to
add to docker base image  
# Install official PhantomJS release  
# RUN set -x \  
# && mkdir /tmp/phantomjs \  
# && cd /tmp/phantomjs \  
# && wget --no-check-certificate
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 -O - \  
# | tar -xj --strip-components=1 -C /tmp/phantomjs \  
# && mv /tmp/phantomjs/bin/phantomjs /usr/local/bin  
# Github dl as alternative  
RUN set -x \  
&& mkdir /tmp/phantomjs \  
&& cd /tmp/phantomjs \  
&& wget -nv
https://github.com/Medium/phantomjs/releases/download/v$PHANTOMJS_VERSION/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 -O - \  
| tar -xj --strip-components=1 -C /tmp/phantomjs \  
&& mv /tmp/phantomjs/bin/phantomjs /usr/local/bin  
  
# Create application folder and ssh-agent folder  
# Setup rails user group and rails user  
# Set rails:rails as user on app and ssh-agent folder  
RUN mkdir $APP_HOME && \  
mkdir /ssh-agent && \  
groupadd -g 1000 rails && \  
useradd -s /bin/bash -m -d /home/rails -g rails rails && \  
chown rails:rails /app && \  
chown rails:rails /ssh-agent  
  
# Copy docker entry point  
COPY docker-entrypoint.sh /usr/local/bin/  
  
# Make entrypoint executable when building on Windows  
# And backwards compatible entrypoint  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh && ln -s
/usr/local/bin/docker-entrypoint.sh /docker-entrypoint.sh  
  
# Continue as rails user  
USER rails  
  
# Set workdir to /app, so COPY, ADD, RUN and ENTRYPOINT is run within folder  
WORKDIR $APP_HOME  
  
# Add Gemfile  
COPY Gemfile Gemfile.lock package.json yarn.lock ./  
# Install gems  
RUN gem install bundler && bundle install --deployment --without
development:test \--jobs 20 --retry 5 && yarn install  
# Disable skylight dev warning  
RUN skylight disable_dev_warning  
  
# Set entry point to bundle exec, as all cmd's with rails should be prepended  
ENTRYPOINT ["docker-entrypoint.sh"]  

