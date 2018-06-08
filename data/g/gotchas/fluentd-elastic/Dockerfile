# or v0.14-debian-onbuild  
FROM fluent/fluentd:v0.12-debian-onbuild  
  
# below RUN includes plugin as examples elasticsearch is not required  
# you may customize including plugins as you wish  
  
RUN buildDeps="sudo make gcc g++ libc-dev ruby-dev" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& sudo gem install \  
fluent-plugin-elasticsearch \  
&& sudo gem sources --clear-all \  
&& SUDO_FORCE_REMOVE=yes \  
apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
$buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  
  
EXPOSE 42185  

