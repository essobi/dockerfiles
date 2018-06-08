FROM ruby:2.4.2-slim  
MAINTAINER Guglio  
  
ENV ZAMMAD_DIR /opt/zammad  
ENV ZAMMAD_USER zammad  
ENV RAILS_ENV production  
ENV GIT_URL https://github.com/zammad/zammad.git  
ENV GIT_BRANCH stable  
  
  
  
# Install dependencies  
RUN apt-get update  
RUN BUILD_DEPENDENCIES="git nginx build-essential libffi-dev libpq5 libpq-dev
libmysqlclient-dev" \  
set -ex \  
&& apt-get install -y --force-yes --no-install-recommends
${BUILD_DEPENDENCIES} \  
&& gem install foreman \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& sed -i "s/^user.*$/daemon off;/" /etc/nginx/nginx.conf \  
&& rm -f /etc/nginx/conf.d/* /etc/nginx/sites-*/* \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& mkdir -p /var/cache/nginx /var/lib/nginx \  
&& chmod -R og+rwx /etc/nginx/conf.d /var/*/nginx \  
&& chmod og+rwx /var/run  
  
# Install Zammad  
RUN set -ex \  
&& useradd -M -d ${ZAMMAD_DIR} ${ZAMMAD_USER} \  
&& cd $(dirname ${ZAMMAD_DIR}) \  
&& git clone \--depth 1 -b "${GIT_BRANCH}" "${GIT_URL}" \  
&& cd ${ZAMMAD_DIR} \  
&& bundle install --without test development \  
&& contrib/packager.io/fetch_locales.rb \  
&& sed -e 's#.*adapter: postgresql# adapter: nulldb#g' -e 's#.*username:.*#
username: postgres#g' -e 's#.*password:.*# password: \n host: zammad-
postgresql\n#g' < config/database.yml.pkgr > config/database.yml \  
&& bundle exec rake assets:precompile \  
&& rm -f config/database.yml \  
&& rm -rf tmp/cache \  
&& mkdir -p ${ZAMMAD_DIR}/storage \  
&& chown -R ${ZAMMAD_USER}:${ZAMMAD_USER} ${ZAMMAD_DIR} \  
&& chmod -R og+rwx ${ZAMMAD_DIR}/log \  
&& chmod -R og+rwx ${ZAMMAD_DIR}/tmp \  
&& chmod -R og+rwx ${ZAMMAD_DIR}/storage \  
&& chmod -R og+rwx ${ZAMMAD_DIR}/public/assets/images  
  
# Copy configuration into container  
COPY Procfile* ${ZAMMAD_DIR}/  
COPY database.yml ${ZAMMAD_DIR}/config/  
COPY zammad.conf /etc/nginx/conf.d/  
  
# Add entrypoint and link log files  
COPY entrypoint.sh /  
RUN chown ${ZAMMAD_USER}:${ZAMMAD_USER} /entrypoint.sh \  
&& chmod +x /entrypoint.sh \  
&& ln -sf /dev/stdout ${ZAMMAD_DIR}/log/production.log \  
&& ln -sf /dev/stdout ${ZAMMAD_DIR}/log/scheduler_out.log \  
&& ln -sf /dev/stderr ${ZAMMAD_DIR}/log/scheduler_err.log \  
&& ln -sf /dev/stdout ${ZAMMAD_DIR}/log/websocket-server_out.log \  
&& ln -sf /dev/stderr ${ZAMMAD_DIR}/log/websocket-server_err.log  
  
# Final steps  
EXPOSE 8080  
USER ${ZAMMAD_USER}  
WORKDIR ${ZAMMAD_DIR}  
  
CMD ["/entrypoint.sh"]  

