FROM ruby:2.3.1-alpine  
MAINTAINER littleman.co <support@littleman.co>  
  
ENV VERSION_GIT_TAG 0.0.2  
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
# The simpest way to do that seems to be to mount the dir as a volume  
# and rebuild the image.  
#VOLUME ["/opt/sensu"]  
COPY /opt/sensu/Gemfile* /opt/sensu/  
  
# nokogiri is an AWS dependency  
RUN bundle install --jobs 10 --quiet --without development test  
RUN cd /tmp && \  
curl -LO https://github.com/andrewhowdencom/sensu-git-tag-
check/releases/download/${VERSION_GIT_TAG}/git-tag-check_linux_amd64.tar.gz &&
\  
gzip -dc git-tag-check_linux_amd64.tar.gz | tar -xvf - -C /usr/local/bin/  
  
# Sensu client port  
EXPOSE 3000  
VOLUME ["/etc/sensu/conf.d"]  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["sensu-client"]  

