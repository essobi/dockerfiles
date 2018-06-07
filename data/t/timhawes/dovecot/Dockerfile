FROM debian:jessie  
  
ENV DOVECOT_VERSION 2.2.34  
ENV DOVECOT_TGZ_URL
http://dovecot.org/releases/2.2/dovecot-$DOVECOT_VERSION.tar.gz  
ENV DOVECOT_GNUPG_KEY C948525140558AC9  
ENV PIGEONHOLE_VERSION 0.4.22  
ENV PIGEONHOLE_TGZ_URL
http://pigeonhole.dovecot.org/releases/2.2/dovecot-2.2-pigeonhole-$PIGEONHOLE_VERSION.tar.gz  
ENV PIGEONHOLE_GNUPG_KEY 04D62B1E3DFBB4F4  
  
RUN installDeps='ca-certificates libsqlite3-0 libldap-2.4-2 libpam0g libexpat1
libssl1.0.0 libpq5 libmysqlclient18' \  
&& buildDeps='wget build-essential libsqlite3-dev libldap2-dev libpam0g-dev
libexpat1-dev libssl-dev libpq-dev libmysqlclient-dev' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $installDeps $buildDeps \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys $DOVECOT_GNUPG_KEY \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
$PIGEONHOLE_GNUPG_KEY \  
&& mkdir /usr/src/dovecot /usr/src/pigeonhole \  
&& cd /usr/src/dovecot \  
&& wget $DOVECOT_TGZ_URL $DOVECOT_TGZ_URL.sig \  
&& gpg --verify dovecot-$DOVECOT_VERSION.tar.gz.sig \  
&& tar -xvf dovecot-$DOVECOT_VERSION.tar.gz --strip-components=1 \  
&& ./configure \  
\--sysconfdir=/etc \  
\--with-solr \  
\--with-pgsql --with-mysql --with-sqlite \  
\--with-shadow --with-pam --with-nss \  
\--with-sql --with-ldap \  
&& make -j"$(nproc)" \  
&& make install \  
&& cd /usr/src/pigeonhole \  
&& wget $PIGEONHOLE_TGZ_URL $PIGEONHOLE_TGZ_URL.sig \  
&& gpg --verify dovecot-2.2-pigeonhole-$PIGEONHOLE_VERSION.tar.gz.sig \  
&& tar -xvf dovecot-2.2-pigeonhole-$PIGEONHOLE_VERSION.tar.gz --strip-
components=1 \  
&& ./configure \  
\--sysconfdir=/etc \  
\--with-ldap=yes \  
&& make -j"$(nproc)" \  
&& make install \  
&& cd / \  
&& rm -r /usr/src/dovecot /usr/src/pigeonhole \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -r /var/lib/apt/lists/* \  
&& groupadd -r dovecot \  
&& groupadd -r dovenull \  
&& useradd -r -M -d /nonexistant -g dovecot -s /bin/false dovecot \  
&& useradd -r -M -d /nonexistant -g dovenull -s /bin/false dovenull  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  
EXPOSE 110 143 993 995 4190  

