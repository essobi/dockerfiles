FROM instructure/canvas-lms:stable  
  
MAINTAINER Maxwell Lincoln <me@maxwelllincoln.com>  
  
ENV CANVAS_LMS_ADMIN_EMAIL admin@example.edu  
ENV CANVAS_LMS_ADMIN_PASSWORD something-secret  
ENV CANVAS_LMS_ACCOUNT_NAME "Docker Canvas"  
ENV CANVAS_LMS_STATS_COLLECTION opt_out  
ENV DOMAIN_NAME "localhost"  
ENV FILE_STORAGE local  
ENV FILE_STORAGE_PREFIX /tmp/files  
ENV FORCE_SSL true  
ENV OUTGOING_MAIL_ADDRESS canvas@canvas.docker  
ENV OUTGOING_MAIL_DOMAIN canvas.docker  
ENV OUTGOING_MAIL_METHOD sendmail  
ENV OUTGOING_MAIL_NAME "Instructure Canvas"  
ENV REDIS_HOST redis  
  
USER root  
  
COPY entrypoint /usr/src/entrypoint  
RUN chmod +x /usr/src/entrypoint  
  
RUN touch /usr/src/app/config/environments/production-local.rb  
RUN echo "config.force_ssl = $FORCE_SSL" >>
/usr/src/app/config/environments/production-local.rb  
RUN chmod +x /usr/src/app/config/environments/production-local.rb  
  
USER docker  
  
COPY config/amazon_s3.yml /usr/src/app/config/amazon_s3.yml  
COPY config/cache_store.yml /usr/src/app/config/cache_store.yml  
COPY config/database.yml /usr/src/app/config/database.yml  
COPY config/delayed_jobs.yml /usr/src/app/config/delayed_jobs.yml  
COPY config/domain.yml /usr/src/app/config/domain.yml  
COPY config/dynamic_settings.yml /usr/src/app/config/dynamic_settings.yml  
COPY config/external_migration.yml /usr/src/app/config/external_migration.yml  
COPY config/file_store.yml /usr/src/app/config/file_store.yml  
COPY config/outgoing_mail.yml /usr/src/app/config/outgoing_mail.yml  
COPY config/redis.yml /usr/src/app/config/redis.yml  
COPY config/security.yml /usr/src/app/config/security.yml  
  

