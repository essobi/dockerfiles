FROM ruby:2.3  
MAINTAINER Aaron Alexander Israel <aaron.israel@cedis.fu-berlin.de>  
  
RUN echo "# Generate locales" && \  
echo "# Upgrade apt" && \  
sed -i 's/main$/main contrib/g' /etc/apt/sources.list && \  
sed -i 's/httpredir.debian.org/debian.tu-bs.de/g' /etc/apt/sources.list && \  
apt-get update && apt-get upgrade -y && \  
echo "# Install common dev dependencies via apt" && \  
apt-get install -y \  
git curl wget rsync patch build-essential sqlite3 libsqlite3-dev \  
graphviz graphviz-dev libgraphviz-dev \  
imagemagick libmagickwand-dev libfreetype6-dev libfreetype6 libfontconfig \  
openssl libreadline6 libreadline6-dev zlib1g zlib1g-dev libssl-dev libyaml-dev
libpq-dev libxml2-dev libxslt-dev libc6-dev \  
postgresql-client bzip2 nodejs --fix-missing --no-install-recommends&& \  
gem install bundler && \  
ln -s /usr/bin/nodejs /usr/local/bin/node && \  
ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime && \  
apt-get clean  
  
ENV APP_HOME /collection_gatherer  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
  
ADD Gemfile* $APP_HOME/  
  
ENV BUNDLE_GEMFILE=$APP_HOME/Gemfile \  
BUNDLE_JOBS=4 \  
BUNDLE_PATH=/bundle  
#  
# RUN bundle install --jobs $(nproc)  
ADD . $APP_HOME  
  
# VOLUME ["$APP_HOME/public"]  
# EXPOSE 3000  
CMD ./bin/puma -C config/puma.rb  

