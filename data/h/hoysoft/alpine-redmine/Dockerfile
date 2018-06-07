FROM alpine:latest  
MAINTAINER Alexey Ivanov <lexa.ivanov@gmail.com>  
  
ENV REDMINE_VERSION=3.3.2 \  
REDMINE_USER="redmine" \  
REDMINE_HOME="/home/redmine" \  
REDMINE_LOG_DIR="/var/log/redmine" \  
REDMINE_CACHE_DIR="/etc/docker-redmine" \  
RAILS_ENV=production  
  
ENV REDMINE_INSTALL_DIR="${REDMINE_HOME}/redmine" \  
REDMINE_DATA_DIR="${REDMINE_HOME}/data" \  
REDMINE_BUILD_DIR="${REDMINE_CACHE_DIR}/build" \  
REDMINE_RUNTIME_DIR="${REDMINE_CACHE_DIR}/runtime"  
LABEL org.label-schema.docker.dockerfile="./Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.name="redmine-alpine" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/inspired-geek/redmine-alpine" \  
org.label-schema.version="latest"  
  
ENV BRANCH_NAME=master \  
RAILS_ENV=production  
  
WORKDIR ${REDMINE_INSTALL_DIR}  
  
RUN addgroup -S redmine \  
&& adduser -S -G redmine redmine \  
&& apk --no-cache add --virtual .run-deps \  
mariadb-client-libs \  
sqlite-libs \  
imagemagick \  
tzdata \  
ruby \  
ruby-bigdecimal \  
ruby-bundler \  
tini \  
su-exec \  
bash \  
&& apk --no-cache add --virtual .build-deps \  
build-base \  
ruby-dev \  
libxslt-dev \  
imagemagick-dev \  
mariadb-dev \  
sqlite-dev \  
linux-headers \  
patch \  
coreutils \  
curl \  
git \  
&& echo 'gem: --no-document' > /etc/gemrc \  
&& gem update --system \  
&& git clone -b ${BRANCH_NAME} https://github.com/redmine/redmine.git . \  
&& rm -rf files/delete.me log/delete.me .git test\  
&& mkdir -p tmp/pdf public/plugin_assets \  
&& chown -R redmine:redmine ./\  
&& for adapter in mysql2 sqlite3; do \  
echo "$RAILS_ENV:" > ./config/database.yml; \  
echo " adapter: $adapter" >> ./config/database.yml; \  
bundle install --without development test; \  
done \  
&& rm ./config/database.yml \  
&& rm -rf /root/* `gem env gemdir`/cache \  
&& apk --purge del .build-deps  
  
# VOLUME ${REDMINE_INSTALL_DIR}/files  
VOLUME ["${REDMINE_DATA_DIR}", "${REDMINE_LOG_DIR}"]  
  
# COPY assets/build/ ${REDMINE_BUILD_DIR}/  
# RUN bash ${REDMINE_BUILD_DIR}/install.sh  
COPY assets/runtime/ ${REDMINE_RUNTIME_DIR}/  
# COPY assets/tools/ /usr/bin/  
COPY docker-entrypoint.sh /sbin/docker-entrypoint.sh  
RUN chmod 755 /sbin/docker-entrypoint.sh  
ENTRYPOINT ["/sbin/docker-entrypoint.sh"]  
  
EXPOSE 3000  
CMD ["rails", "server", "-b", "0.0.0.0"]  

