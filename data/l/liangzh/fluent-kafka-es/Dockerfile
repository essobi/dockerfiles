FROM fluent/fluentd:v0.12-debian-onbuild  
  
# below RUN includes plugin as examples elasticsearch is not required  
# you may customize including plugins as you wish  
ENV TIME_ZONE Asia/Shanghai  
  
RUN buildDeps="sudo make gcc g++ libc-dev ruby-dev" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& apt-get install -y libgssapi-krb5-2 \  
build-essential \  
autoconf \  
automake \  
libtool \  
libsnappy-dev \  
&& sudo gem install \  
snappy \  
fluent-plugin-elasticsearch \  
fluent-plugin-kafka \  
&& sudo gem sources --clear-all \  
&& SUDO_FORCE_REMOVE=yes \  
apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
$buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem \  
&& echo "${TIME_ZONE}" > /etc/timezone \  
&& ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata

