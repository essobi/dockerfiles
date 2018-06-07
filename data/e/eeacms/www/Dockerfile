FROM eeacms/kgs:18.6.5  
ENV portal_url=https://www.eea.europa.eu \  
AOA_MAP_TILES=http://aoa.ew.eea.europa.eu/maptiles/ \  
AOA_PORTAL_URL=http://aoa.ew.eea.europa.eu/ \  
PROD_SENTRY_DSN=https://8c9dd62711a841c8935c4d49ca78865a@sentry.io/228226 \  
STAGING_SENTRY_DSN=https://90ad76b69bf340aea06613147716cd95@sentry.io/240604 \  
DEVEL_SENTRY_DSN=https://52bee1ebb7d8494b899d066345856517@sentry.io/218533 \  
EEALOGINAGENT_LOG=/data/eea.controlpanel \  
EEACPBINSTANCESAGENT_LOG=/data/eea.controlpanel \  
RABBITMQ_HOST=rabbitmq \  
RABBITMQ_PORT=5672 \  
RABBITMQ_USER=guest \  
RABBITMQ_PASS=guest \  
saved_resources=/data/www-static-resources \  
zope_i18n_compile_mo_files=true \  
WARMUP_BIN=/plone/instance/bin/warmup \  
WARMUP_INI=/plone/instance/warmup.ini \  
WARMUP_HEALTH_THRESHOLD=50000 \  
EDW_LOGGER_PUBLISHER=false \  
RELSTORAGE_KEEP_HISTORY=false  
  
COPY src/plone/* /plone/instance/  
COPY src/docker/* /  
RUN /docker-setup.sh  

