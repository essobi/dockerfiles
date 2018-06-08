FROM fluent/fluentd:v0.12.33-debian-onbuild  
  
USER root  
  
RUN buildDeps="sudo make gcc g++ libc-dev ruby-dev" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
# cutomize following instruction as you wish  
&& sudo -u fluent gem install \  
fluent-plugin-google-cloud \  
fluent-plugin-forest \  
fluent-plugin-secure-forward \  
fluent-plugin-elasticsearch \  
  
&& sudo -u fluent gem sources --clear-all \  
&& SUDO_FORCE_REMOVE=yes \  
apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
$buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  
  
USER fluent  

