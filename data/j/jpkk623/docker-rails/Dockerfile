FROM ruby:2.4.2-alpine  
  
ENV LANG C.UTF-8  
ENV APP_ROOT /app  
ENV BUNDLE_PATH $APP_ROOT/vendor/bundle  
ENV TZ Asia/Tokyo  
  
WORKDIR $APP_ROOT  
RUN apk upgrade \--no-cache && \  
apk --update add \--no-cache \  
build-base \  
bash \  
git \  
vim \  
less \  
libxml2-dev \  
libxslt-dev \  
libgcrypt-dev \  
libc6-compat \  
xz-dev \  
tzdata \  
postgresql \  
postgresql-dev \  
postgresql-client \  
nodejs \  
imagemagick \  
imagemagick-dev  
  
RUN npm install --global yarn  
  
RUN gem install bundler  
RUN bundle config \--global build.nokogiri --use-system-libraries  
RUN gem install nokogiri  
  
COPY . $APP_ROOT  

