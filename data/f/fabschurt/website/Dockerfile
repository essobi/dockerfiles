FROM alpine:3.5  
MAINTAINER Fabien Schurter <fabien@fabschurt.com>  
  
ARG ENVIRONMENT=prod  
ARG ENABLE_WATCH=0  
ENV JEKYLL_ENV="$ENVIRONMENT"  
  
COPY . /opt/codebase  
WORKDIR /opt/codebase  
RUN apk update --no-cache && \  
apk add \  
nodejs \  
ruby-io-console \  
ruby-json \  
ruby-bundler \  
&& \  
apk add --virtual .build \  
git \  
ruby-dev \  
libffi-dev \  
make \  
g++ \  
&& \  
npm install --unsafe-perm $([ "$ENVIRONMENT" == 'dev' ] || echo '--production
--no-spin') && \  
addgroup -S jekyll && \  
adduser -SDH -s /sbin/nologin -G jekyll jekyll && \  
chgrp -R jekyll . && \  
chmod -R g+rX . && \  
chmod -R g+w web && \  
apk del --purge .build && \  
apk add ruby && \  
rm -rf /tmp/* \  
/var/cache/apk/* \  
/root/.bundle/* \  
/root/.npm/* \  
/root/.cache/*  
  
EXPOSE 4000  
USER jekyll  
CMD bundle exec jekyll serve \  
$([ "$JEKYLL_ENV" == 'prod' ] && echo '--no-watch' || echo '--trace
--force_polling') \  
\--host 0.0.0.0 --source app/jekyll --destination web  

