FROM ruby:2.3-alpine  
  
MAINTAINER Eric Biven <eric@biven.us>  
  
ENV RAILS_VERSION="5.0.0" \  
BUILD_PACKAGES="curl-dev build-base openssh" \  
DEV_PACKAGES="tzdata libxml2 libxml2-dev libxslt libxslt-dev postgresql-dev \  
imagemagick imagemagick-dev mysql-dev sqlite-dev git nodejs" \  
RUBY_GEMS="nokogiri rake minitest execjs bcrypt sass coderay coffee-script-
source \  
debug_inspector orm_adapter ffi formatador rb-fsevent lumberjack nenv \  
shellany slop multi_json pg puma tilt turbolinks-source uglifier \  
coffee-script rb-inotify notiffany pry turbolinks bootstrap-sass \  
listen pry-rails jbuilder spring guard spring-watcher-listen \  
coffee-rails responders jquery-rails web-console sass-rails"  
  
RUN \  
apk --update --upgrade add $BUILD_PACKAGES $DEV_PACKAGES && \  
rm /var/cache/apk/* && \  
gem install -N $RUBY_GEMS && \  
gem install -N rails --version "$RAILS_VERSION" && \  
echo 'gem: --no-document' >> ~/.gemrc && \  
cp ~/.gemrc /etc/gemrc && \  
chmod uog+r /etc/gemrc && \  
# cleanup and settings  
# bundle config --global build.nokogiri "--use-system-libraries" && \  
# bundle config --global build.nokogumbo "--use-system-libraries" && \  
rm -rf /usr/lib/lib/ruby/gems/*/cache/* && \  
rm -rf ~/.gem  
  
CMD [ "/bin/sh" ]  

