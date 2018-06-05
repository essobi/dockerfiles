FROM debian:stretch  
  
RUN \  
apt-get -y -q update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y -q --no-install-recommends
install apt-transport-https curl ca-certificates gnupg dirmngr \  
&& echo "deb https://deb.nodesource.com/node_8.x stretch main" >
/etc/apt/sources.list.d/nodesource.list \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list \  
&& curl -sS https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
\- \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& apt-get -y -q update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y -q --no-install-recommends
install \  
build-essential \  
nodejs \  
yarn \  
jq \  
libfreetype6 \  
libfontconfig1 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm /var/log/dpkg.log \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64" \  
&& chmod +x /usr/local/bin/gosu  
  
ENV LANG=C  
ENV NODE_PATH="/usr/local/lib/node_modules:/usr/lib/node_modules"  
  
RUN mkdir -p /var/www  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["start"]  

