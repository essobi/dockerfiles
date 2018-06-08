FROM cloudgear/build-deps:14.04  
  
ENV RUBY_VERSION 2.0  
ENV REALLY_GEM_UPDATE_SYSTEM 1  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
C3173AA6 && \  
echo deb http://ppa.launchpad.net/brightbox/ruby-ng-experimental/ubuntu trusty
main > /etc/apt/sources.list.d/brightbox-ruby-ng-experimental-trusty.list && \  
apt-get update -q && apt-get install -yq --no-install-recommends \  
ruby$RUBY_VERSION \  
ruby$RUBY_VERSION-dev \  
ruby-switch && \  
  
ruby-switch --set ruby$RUBY_VERSION && \  
  
echo 'gem: --no-document' > /etc/gemrc && \  
gem update \--system && \  
gem install bundler  
  
RUN rm -rf /var/lib/apt/lists/* && \  
truncate -s 0 /var/log/*log  
  
CMD ["/usr/bin/ruby"]

