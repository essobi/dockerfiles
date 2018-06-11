FROM ruby:2.4.1-slim  
MAINTAINER Zammad <info@zammad.org>  
ARG BUILD_DATE  
  
ENV ZAMMAD_DIR /home/zammad  
ENV ZAMMAD_TMP_DIR /tmp/zammad  
ENV ZAMMAD_USER zammad  
ENV RAILS_ENV production  
ENV RAILS_SERVER puma  
ENV GIT_URL https://github.com/zammad/zammad.git  
ENV GIT_BRANCH 2.1.1  
ENV GOSU_VERSION 1.10  
ENV BACKUP_SLEEP 86400  
ENV HOLD_DAYS 10  
ENV BACKUP_DIR /var/tmp/zammad  
  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="Zammad" \  
org.label-schema.license="AGPL-3.0" \  
org.label-schema.description="Docker container for Zammad" \  
org.label-schema.url="https://zammad.org" \  
org.label-schema.vcs-url="https://github.com/zammad/zammad" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vendor="Zammad" \  
org.label-schema.schema-version="1.2" \  
org.label-schema.docker.cmd="sysctl -w vm.max_map_count=262144;docker-compose
up --build"  
  
RUN apt-get update; apt-get -yqq install wget \  
&& wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key
add - \  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main" >>
/etc/apt/sources.list.d/postgres.list \  
&& apt-get update;apt-get -yqq install postgresql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
# install dependencies, GOSU & zammad  
RUN BUILD_DEPENDENCIES="git build-essential libffi-dev libpq5 libpq-dev rsync"
\  
GOSU_DEPENDENCIES="ca-certificates wget" \  
set -ex \  
&& apt-get update && apt-get install -y --force-yes --no-install-recommends
${BUILD_DEPENDENCIES} ${GOSU_DEPENDENCIES} && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -rf "${GNUPGHOME}" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& useradd -M -d ${ZAMMAD_DIR} -s /bin/bash ${ZAMMAD_USER} \  
&& cd $(dirname ${ZAMMAD_TMP_DIR}) \  
&& git clone \--depth 1 -b "${GIT_BRANCH}" "${GIT_URL}" \  
&& cd ${ZAMMAD_TMP_DIR} \  
&& bundle install --without test development mysql \  
&& contrib/packager.io/fetch_locales.rb \  
&& sed -e 's#.*adapter: postgresql# adapter: nulldb#g' -e 's#.*username:.*#
username: postgres#g' -e 's#.*password:.*# password: \n host: zammad-
postgresql\n#g' < config/database.yml.pkgr > config/database.yml \  
&& bundle exec rake assets:precompile \  
&& sed -e 's#.*adapter: postgresql# adapter: postgresql#g' -e
's#.*username:.*# username: postgres#g' -e 's#.*password:.*# password: \n
host: zammad-postgresql\n#g' < config/database.yml.pkgr > config/database.yml
\  
&& rm -r tmp/cache \  
&& chown -R ${ZAMMAD_USER}:${ZAMMAD_USER} ${ZAMMAD_TMP_DIR}  
  
COPY docker-entrypoint.sh /  
RUN chown ${ZAMMAD_USER}:${ZAMMAD_USER} /docker-entrypoint.sh && chmod +x
/docker-entrypoint.sh  
WORKDIR ${ZAMMAD_DIR}  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["zammad-railsserver"]  

