FROM ruby:2.3-alpine  
MAINTAINER littleman.co <support@littleman.co>  
  
# Sensu core and plugin dependencies  
RUN apk add -qU --no-cache \  
build-base \  
curl-dev \  
libffi-dev \  
ruby-bundler \  
ruby-dev \  
ruby-io-console \  
# sensu-plugins-aws dependencies  
libxml2-dev \  
libxslt-dev && \  
apk add \  
\--update \  
\--repository http://dl-2.alpinelinux.org/alpine/edge/community/ \  
tini  
  
# Sensu dirs  
RUN mkdir -p \  
/opt/sensu \  
/etc/sensu/conf.d \  
/etc/sensu/ssl  
  
WORKDIR /opt/sensu  
  
# install Sensu core and Ruby plugins  
#  
# NOTE that when updating Gemfile, you should also add the updated  
# Gemfile.lock into the image.  
#  
# The easiest way to do this is:  
# - build manually  
# - run image with a mount volume  
# - copy the generated Gemfile.lock to your host machine via the volume  
# - git commit Gemfile.lock  
#  
# this will result in dockerhub building using updated Gemfile.lock,  
# instead of having to regenerate it (error prone, slow)  
COPY /opt/sensu/Gemfile* /opt/sensu/  
  
# nokogiri is an AWS dependency  
RUN bundle install --jobs 10 --quiet --without development test  
  
# Sensu client port  
EXPOSE 3000  
VOLUME ["/etc/sensu/conf.d"]  
  
ENTRYPOINT ["tini", "--"]  
CMD ["sensu-client"]  

