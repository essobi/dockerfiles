FROM blendle/base:3.2  
MAINTAINER Jean Mertz <jean@blendle.com>  
  
WORKDIR /home  
  
CMD ["/bin/sh"]  
  
# CI dependencies  
RUN bnl-apk-install-download-deps  
RUN bnl-apk-install-build-deps  
RUN apk-install socat bash ca-certificates git openssh coreutils  
  
# Ruby dependencies  
RUN apk-install ruby ruby-dev libxslt-dev zlib-dev libxml2-dev  
RUN gem install --no-document bundler  
  
# Gem dependencies  
RUN apk-install libffi libffi-dev  
  
# Postgres dependencies  
RUN apk-install postgresql-client  
  
# NodeJS dependencies  
RUN apk-install nodejs  
  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
  
RUN gem install --no-document io-console  
  
RUN bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin" \  
&& bundle config --global frozen 1 \  
&& bundle config --global retry 3 \  
&& bundle config build.nokogiri --use-system-libraries  
  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
  
# Docker in Docker  
ENV LOG=file  
ENV SECONDS=120  
VOLUME /var/lib/docker  
  
RUN apk-install iptables lxc e2fsprogs wget docker perl device-mapper  
  
RUN wget -qO- https://get.docker.com/builds/Linux/x86_64/docker-1.6.2 >
/usr/bin/docker  
RUN wget -qO-
https://raw.githubusercontent.com/jpetazzo/dind/master/wrapdocker >
/usr/local/bin/wrapdocker  
RUN chmod +x /usr/bin/docker /usr/local/bin/wrapdocker  
  
COPY bin/git-reset-mtime /usr/local/bin/git-reset-mtime  

