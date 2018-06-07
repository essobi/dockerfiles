FROM ruby:2.2-slim  
MAINTAINER kristopher.michalski@gmail.com  
  
# Set all environment variables at once  
ENV GOSU_VERSION=1.10 \  
GEM_HOME=/home/app/bundle \  
BUNDLE_PATH=/home/app/bundle \  
BUNDLE_APP_CONFIG=/home/app/bundle \  
APP=/home/app/webapp \  
PATH=/home/app/webapp/bin:/home/app/bundle/bin:$PATH \  
DB_ADAPTER=sqlite3  
  
# Install bash, less, nodejs, db clients and gosu  
# Create app directory and set permissions  
# Remove cache  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
bash less nodejs \  
build-essential ruby-dev \  
libc-dev libffi-dev \  
mysql-client postgresql-client sqlite3 \  
libmysqlclient-dev libpq-dev libsqlite3-dev \  
libxml2-dev libxslt-dev \  
tzdata \  
ca-certificates wget \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \--keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg \--batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& addgroup \--gid 1000 app \  
&& adduser \--gecos "" \--uid 1000 --disabled-password --ingroup app --shell
/bin/bash app \  
&& mkdir -p "$APP" "$GEM_HOME/bin" \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /home/app/.gemrc \  
&& chown -R app:app /home/app \  
&& apt-get clean \  
&& rm -rf '/var/lib/apt/lists/*' '/tmp/*' '/var/tmp/*'  
  
WORKDIR $APP  
COPY start.sh template.rb entrypoint.sh install_rails.sh /home/app/  
  
ENTRYPOINT ["/home/app/entrypoint.sh"]  
CMD ["/home/app/start.sh"]  

