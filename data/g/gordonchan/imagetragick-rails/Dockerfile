FROM ruby:2.3.1-slim  
MAINTAINER Gordon Chan <github.com/gchan>  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
nodejs \  
libsqlite3-dev \  
file \  
libmagickcore-6.q16-2-extra=8:6.8.9.9-5+deb8u1 \  
imagemagick-common=8:6.8.9.9-5+deb8u1 \  
imagemagick=8:6.8.9.9-5+deb8u1 \  
imagemagick-6.q16=8:6.8.9.9-5+deb8u1 \  
libmagickcore-6.q16-2=8:6.8.9.9-5+deb8u1 \  
libmagickwand-6.q16-2=8:6.8.9.9-5+deb8u1 \  
\--fix-missing \  
\--no-install-recommends  
  
ENV INSTALL_PATH /app  
RUN mkdir -p $INSTALL_PATH  
  
WORKDIR $INSTALL_PATH  
  
COPY Gemfile Gemfile  
COPY Gemfile.lock Gemfile.lock  
RUN gem install bundler  
RUN bundle install  
  
COPY . .  
  
ENV RAILS_ENV=production  
ENV RAILS_SERVE_STATIC_FILES=true  
  
RUN rake SECRET_KEY_BASE=pickasecuretoken assets:precompile  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["rails", "s", "--binding=0.0.0.0"]  

