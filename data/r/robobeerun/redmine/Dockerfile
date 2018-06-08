FROM redmine:3.4.5  
LABEL maintainer "Erwin Mueller <erwin.mueller@deventm.com>"  
  
ARG APT_CACHE  
  
RUN set -x \  
# Optional add proxy entries for apt.  
&& if [ -n "${APT_CACHE}" ]; then \  
echo Acquire::ftp::Proxy \"$APT_CACHE\"; >> /etc/apt/apt.conf.d/08proxy;\  
echo Acquire::http::Proxy \"$APT_CACHE\"; >> /etc/apt/apt.conf.d/08proxy;\  
echo Acquire::https::Proxy \"$APT_CACHE\"; >> /etc/apt/apt.conf.d/08proxy;\  
fi  
  
ENV WEB_ROOT="/var/www/html" \  
WEB_USER="redmine" \  
SRC_DIR="/usr/src/redmine"  
  
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
&& apt-get update && apt-get install -y --no-install-recommends $buildDeps \  
rsync \  
unzip \  
coreutils \  
curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo 'gem "puma", "3.4.0"' >> Gemfile \  
&& echo 'gem "piwik_analytics", "~> 1.0.2"' >> Gemfile \  
&& echo 'gem "temple", "~> 0.8.0"' >> Gemfile \  
&& echo 'gem "dalli", "~> 2.7.8"' >> Gemfile \  
&& for adapter in mysql2 postgresql sqlite3; do \  
echo "$RAILS_ENV:" > ./config/database.yml; \  
echo " adapter: $adapter" >> ./config/database.yml; \  
bundle install --without development test; \  
cp Gemfile.lock "Gemfile.lock.${adapter}"; \  
done \  
&& rm ./config/database.yml \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& chown ${WEB_USER}.${WEB_USER} /usr/local/bundle  
  
RUN set -x \  
&& mkdir -p $WEB_ROOT \  
&& chown -R ${WEB_USER}.${WEB_USER} $WEB_ROOT \  
&& chown -R ${WEB_USER} /usr/local/bundle \  
&& mkdir -p /home/redmine \  
&& chown -R ${WEB_USER}.${WEB_USER} /home/redmine \  
&& mkdir -p /var/run/puma \  
&& chown -R ${WEB_USER}.${WEB_USER} /var/run/puma  
  
ADD rootfs/ /  
  
RUN set -x \  
&& chmod +x /*.sh  
  
RUN set -x \  
&& export DEBUG=false \  
&& /install_plugins.sh  
  
RUN set -x \  
&& export DEBUG=false \  
&& /install_themes.sh  
  
ENV BUNDLE_GEMFILE=/var/www/html/Gemfile \  
PUMA_MIN_THREADS=8 \  
PUMA_MAX_THREADS=16 \  
PUMA_CLUSTER_WORKERS=2 \  
PUMA_WORKER_TIMEOUT=120 \  
PUMA_WORKER_BOOT_TIMEOUT=120 \  
PIWIK_ID_SITE=1 \  
PIWIK_URL=localhost \  
PIWIK_USE_ASYNC=false \  
PIWIK_DISABLED=true  
  
# Puma Control App TCP Socket  
EXPOSE 9293  
  
VOLUME ["/var/www/html"]  
  
USER ${WEB_USER}  
  
WORKDIR ${WEB_ROOT}  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["puma", "-C", "./config/config.rb"]  

