FROM ruby:2.4.4-alpine3.6  
WORKDIR /janna  
  
ARG BUILD_DEPS=' \  
ruby-dev \  
build-base \  
libxml2-dev \  
libxslt-dev \  
libffi-dev'  
ARG RUNTIME_DEPS=' \  
curl'  
ENV LANG C.UTF-8  
RUN apk add --no-cache $RUNTIME_DEPS  
  
COPY Gemfile.lock .  
COPY Gemfile .  
  
RUN apk add --no-cache --virtual .build-deps $BUILD_DEPS && \  
bundle install --jobs=4 --retry=4 && \  
apk del .build-deps && \  
rm -rf /var/cache/apk/*  
  
COPY . .  
  
ENTRYPOINT ["bundle", "exec"]  
CMD ["shotgun", "--server", "puma", "--host", "0.0.0.0", "--port", "4567"]  

