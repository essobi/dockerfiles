FROM ruby:2.3.4-alpine  
  
RUN apk upgrade --no-cache && \  
apk --update add --no-cache \  
build-base \  
bash \  
libgcrypt-dev \  
tzdata \  
mysql-client \  
mariadb-dev \  
nodejs \  
libxml2-dev \  
libxslt-dev \  
imagemagick \  
imagemagick-dev \  
&& bundle config build.nokogiri --use-system-libraries \  
&& gem install nokogiri -v '1.6.8'  
  
ENV app /app  
RUN mkdir $app  
WORKDIR $app  
  
ENV BUNDLE_PATH /app/vendor/bundle  
  
ADD . $app  

