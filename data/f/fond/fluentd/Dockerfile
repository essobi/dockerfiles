FROM fluent/fluentd:stable-debian-onbuild  
  
RUN buildDeps="make gcc g++ libc-dev ruby-dev" \  
&& pluginDeps="fluent-plugin-s3" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& gem install $pluginDeps \  
&& gem sources --clear-all \  
&& apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
$buildDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 24224 9880  

