FROM ruby:2.3-alpine  
  
RUN apk add --no-cache \  
mysql-dev \  
mysql-client \  
cups-libs \  
openssh \  
nodejs \  
git \  
g++ \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
make \  
tzdata  
  
ENV APP_HOME /app  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
ADD Gemfile* $APP_HOME/  
  
ENV BUNDLE_GEMFILE=$APP_HOME/Gemfile \  
BUNDLE_JOBS=2 \  
BUNDLE_PATH=/bundle  
  
RUN bundle install  
  
ADD . $APP_HOME  
  
EXPOSE 3000  

