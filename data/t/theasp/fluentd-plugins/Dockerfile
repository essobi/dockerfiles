FROM fluent/fluentd:edge-debian  
  
# below RUN includes plugin as examples elasticsearch is not required  
# you may customize including plugins as you wish  
  
ENV BUILD_DEPS="sudo make gcc g++ rake patch libc-dev ruby-dev zlib1g-dev
libcurl4-openssl-dev libpq-dev libssl-dev libsqlite3-dev default-
libmysqlclient-dev libgeoip-dev libsasl2-dev libxml2-dev"  
  
RUN set -ex ; \  
sed -r -i -e 's! main! main contrib non-free!g' /etc/apt/sources.list; \  
cat /etc/apt/sources.list ; \  
apt-get update -q; \  
apt-cache search '.*mysql.*-dev' ; \  
apt-get install -qy --no-install-recommends $BUILD_DEPS; \  
gem search ^fluent-plugin- | cut -f 1 -d ' ' | egrep -v '(aurora|aerospike)' |
xargs -r sudo gem install || true ; \  
sudo gem sources --clear-all ; \  
apt-get purge -qy $(dpkg-query --show --showformat '${Package}\n' '*-dev'); \  
# SUDO_FORCE_REMOVE=yes apt-get purge -qy --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS ; \  
rm -rf /var/lib/apt/lists/* /home/fluent/.gem/ruby/*/cache/*.gem  

