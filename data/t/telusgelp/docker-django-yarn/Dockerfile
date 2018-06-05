FROM telusgelp/django:3.6-uwsgi  
  
# allow apt to use https transport  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
apt-transport-https \  
; \  
rm -rf /var/lib/apt/lists/*;  
  
# Yarn Apt Repository  
RUN set -ex; \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -; \  
echo 'deb https://dl.yarnpkg.com/debian/ stable main' >
/etc/apt/sources.list.d/yarn.list;  
  
# Node Apt Repository  
RUN set -ex; \  
curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -;
\  
echo "deb https://deb.nodesource.com/node_8.x jessie main" >
/etc/apt/sources.list.d/nodesource.list; \  
echo "deb-src https://deb.nodesource.com/node_8.x jessie main" >>
/etc/apt/sources.list.d/nodesource.list;  
  
# install libraries  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
yarn \  
; \  
rm -rf /var/lib/apt/lists/*;  

