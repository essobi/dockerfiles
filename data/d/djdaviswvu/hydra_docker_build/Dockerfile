FROM ruby:2.3  
  
ENV BUILD_PACKAGES = ""  
  
# Install capybara-webkit deps  
RUN apt-get update \  
&& apt-get install -y xvfb cron git imagemagick gcc g++ make patch binutils
libc6-dev libjemalloc-dev libffi-dev libssl-dev libyaml-dev zlib1g-dev libgmp-
dev libxml2-dev libxslt1-dev libpq-dev libreadline-dev libsqlite3-dev
libmysqlclient-dev tzdata nano  
  
# Node.js  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs  
  
# yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -\  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install -y yarn  
  
# Install our dependencies and rails  
RUN \  
gem install bundler \  
&& gem install rails

