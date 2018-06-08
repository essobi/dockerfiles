# modified from https://github.com/tyage/slack-
patron/blob/v1.7.1/logger/Dockerfile and https://github.com/tyage/slack-
patron/blob/v1.7.1/viewer/Dockerfile  
FROM ruby:2.3-alpine  
  
ARG SRCDIR=/usr/local/slack-patron  
  
RUN set -x && \  
apk add --update gettext  
  
RUN mkdir -p ${SRCDIR}  
WORKDIR ${SRCDIR}  
COPY slack-patron/Gemfile slack-patron/Gemfile.lock ./  
RUN set -x && \  
echo 'gem: --no-document' >> /etc/gemrc && \  
apk add --update \  
build-base \  
openssl \  
nodejs && \  
bundle install  
COPY slack-patron ${SRCDIR}  
RUN ./viewer/setup.sh  
  
COPY config.yml.template ${SRCDIR}  
COPY entrypoint.sh ${SRCDIR}  
  
CMD ["./entrypoint.sh"]  
EXPOSE 9292  

