# TODO: start direcly from ruby image?  
FROM maestrano/web-ruby:2.3  
MAINTAINER developpers@maestrano.com  
  
# Cache folder  
ENV YARN_CACHE_FOLDER /cache/yarn  
ENV bower_storage__packages /cache/bower  
ENV GEM_SPEC_CACHE /cache/gem  
  
# Install yarn  
ADD https://dl.yarnpkg.com/debian/pubkey.gpg /tmp/yarn-pubkey.gpg  
RUN set -ex && \  
apt-key add /tmp/yarn-pubkey.gpg && rm /tmp/yarn-pubkey.gpg && \  
echo "deb http://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list && \  
apt-get -y update && \  
apt-get install -y --no-install-recommends yarn && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# TODO: replace by `rake mnoe:frontend:install_dependencies`?  
RUN yarn global add bower  
  
WORKDIR /app  
ADD Gemfile Gemfile.lock /app/  
  
RUN set -ex \  
&& export BUNDLE_JOBS=${BUNDLE_JOBS:-$(nproc)} \  
# default to number of cores  
&& echo 'gem: --no-document' >> ~/.gemrc \  
&& gem install bundler \  
&& bundle install --deployment --without development test  
  
COPY docker/docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
ADD . /app  
  
# Build frontend  
RUN set -ex \  
&& echo '{ "allow_root": true }' > /root/.bowerrc \  
&& SECRET_KEY_BASE=secret bundle exec rake mnoe:frontend:build  

