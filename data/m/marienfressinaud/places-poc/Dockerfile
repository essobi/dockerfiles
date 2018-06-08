FROM ruby:2.4-alpine  
MAINTAINER Marien Fressinaud <dev@marienfressinaud.fr>  
  
EXPOSE 3000  
WORKDIR /app/  
COPY Gemfile Gemfile.lock /app/  
  
ENV RAILS_ENV production  
ENV RAILS_LOG_TO_STDOUT true  
  
RUN apk add --no-cache \  
nodejs \  
postgresql-client \  
tzdata \  
&& npm install npm@5 -g  
RUN apk --update add --virtual build-dependencies \  
build-base \  
ruby-dev \  
openssl-dev \  
postgresql-dev \  
libc-dev \  
linux-headers \  
cmake \  
gmp-dev  
  
RUN gem install bundler \  
&& bundle install --deployment --without test development \  
&& apk del build-dependencies  
  
RUN npm install yarn -g  
RUN mkdir -p /app/public/assets  
  
COPY . /app  
  
VOLUME /app/public/assets  
  
CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]  

