FROM ruby:2.4  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r redmine && useradd -r -g redmine redmine  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
imagemagick \  
libmysqlclient18 \  
libpq5 \  
libsqlite3-0 \  
\  
bzr \  
git \  
mercurial \  
openssh-client \  
subversion \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/src/redmine  
ENV RAILS_ENV development  
  
RUN svn export \--trust-server-cert --force \  
https://svn.redmine.org/redmine/trunk /usr/src/redmine \  
&& mkdir -p tmp/pdf public/plugin_assets \  
&& chown -R redmine:redmine ./  
  
COPY database.yml /usr/src/redmine/config/database.yml  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN buildDeps=' \  
gcc \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libpq-dev \  
libsqlite3-dev \  
make \  
patch \  
' \  
&& set -ex \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& bundle install \  
&& rails db:migrate \  
&& rails config/initializers/secret_token.rb \  
&& apt-get purge -y --auto-remove $buildDeps  
  
VOLUME /usr/src/redmine/files  
  
EXPOSE 3000  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["rails", "server", "-b", "0.0.0.0"]  

