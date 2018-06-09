FROM fluent/fluentd:stable-debian-onbuild  
LABEL Maintainer="Sergey Ugdyzhekov, sergey@ugdyzhekov.org"
Description="Fluentd docker image"  
  
USER root  
  
RUN mkdir /var/log/td-agent/ && chown fluent /var/log/td-agent/  
  
RUN buildDeps="sudo make gcc g++ libc-dev ruby-dev" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& sudo -u fluent gem install \  
fluent-plugin-secure-forward \  
fluent-plugin-elasticsearch \  
fluent-plugin-kinesis \  
fluent-plugin-s3 \  
fluent-plugin-influxdb --no-document \  
bigdecimal \  
&& sudo -u fluent gem sources --clear-all \  
&& SUDO_FORCE_REMOVE=yes \  
apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
$buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  
  
USER fluent  
  
EXPOSE 24284  

