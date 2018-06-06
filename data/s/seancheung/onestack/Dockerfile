FROM ubuntu:16.04  
LABEL maintainer="Sean Cheung <theoxuanx@gmail.com>"  
  
ARG MONGO_VERSION=3.6.3  
ARG NODE_VERSION=v9.5.0  
RUN set -x \  
&& apt-get update \  
&& export DEBIAN_FRONTEND="noninteractive" \  
&& echo "Install Dependencies..." \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends curl wget ca-certificates redis-
server mysql-server mysql-client bash openssl supervisor nginx python make g++
\  
&& echo "Downloading [mongodb $MONGO_VERSION]..." \  
&& mkdir -p /tmp/mongodb \  
&& curl -sL https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-${MONGO_VERSION}.tgz | tar zx -C /tmp/mongodb --strip-
components=1 \  
&& cp -r /tmp/mongodb/bin/* /usr/bin \  
&& groupadd -r mongodb \  
&& useradd -r -s /bin/false -g mongodb mongodb \  
&& echo "Downloading [nodejs $NODE_VERSION]..." \  
&& mkdir -p /tmp/nodejs \  
&& curl -sL https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-
linux-x64.tar.gz | tar zx -C /tmp/nodejs --strip-components=1 \  
&& cp -r /tmp/nodejs/bin/* /usr/bin/ \  
&& cp -r /tmp/nodejs/include/* /usr/include/ \  
&& cp -r /tmp/nodejs/lib/* /usr/lib/ \  
&& cp -r /tmp/nodejs/share/* /usr/share/ \  
&& echo "Download and compile [su-exec]..." \  
&& mkdir -p /tmp/su-exec \  
&& curl -sL https://github.com/ncopa/su-exec/tarball/v0.2 | tar zx -C /tmp/su-
exec --strip-components=1 \  
&& make -C /tmp/su-exec \  
&& mv /tmp/su-exec/su-exec /sbin/su-exec \  
&& chmod +x /sbin/su-exec \  
&& echo "Initializing directories..." \  
&& for path in \  
/var/run/mysqld \  
/var/log/mysql \  
/var/opt/mysql \  
; do \  
mkdir -p "$path"; \  
chown mysql:mysql "$path"; \  
done \  
&& for path in \  
/var/run/redis \  
/var/log/redis \  
/var/opt/redis \  
; do \  
mkdir -p "$path"; \  
chown redis:redis "$path"; \  
done \  
&& for path in \  
/var/run/mongodb \  
/var/log/mongodb \  
/var/opt/mongodb \  
; do \  
mkdir -p "$path"; \  
chown mongodb:mongodb "$path"; \  
done \  
&& for path in \  
/var/run/nginx \  
/var/log/nginx \  
; do \  
mkdir -p "$path"; \  
chown www-data:www-data "$path"; \  
done \  
&& rm /etc/nginx/sites-enabled/default \  
&& echo "Clean Up..." \  
&& rm -rf /tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY supervisord.conf /etc/supervisor/  
COPY supervisor /etc/supervisor/conf.d/  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME ["/var/opt/mysql", "/var/opt/redis", "/var/opt/mongodb",
"/etc/supervisor/conf.d", "/etc/nginx/sites-enabled"]  
EXPOSE 3306 6379 27017  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

