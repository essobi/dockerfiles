# We have a range of options for controlling the version: v0.12.36, v0.12,  
# stable, latest  
FROM fluent/fluentd:v0.12-debian  
  
# Essentially copy/paste Fluentd docs to install the necessary Fluentd
plugins.  
# See https://github.com/fluent/fluentd-docker-
image/tree/ad7bb428398237fc1f0a79079f7d0f7cb1375e3a#3-customize-dockerfile-to-
install-plugins-optional  
#  
# We use s3 as short-term storage for the full log stream.  
#  
# We use filter_where (https://github.com/sonots/fluent-plugin-filter_where)  
# to extract metrics from the log stream.  
#  
# We use prometheus to expose the metrics to Prometheus.  
  
RUN buildDeps="sudo make gcc g++ libc-dev ruby-dev" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& sudo gem install \  
fluent-plugin-s3 \  
fluent-plugin-filter_where \  
fluent-plugin-prometheus \  
&& sudo gem sources --clear-all \  
&& SUDO_FORCE_REMOVE=yes \  
apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
$buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  

