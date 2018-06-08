FROM huggla/alpine  
  
USER root  
  
# Build-only variables  
ENV CONFIG_DIR="/etc/postgres" \  
PG_MAJOR="10" \  
PG_VERSION="10.4"  
  
COPY ./start /start  
COPY ./extension/* /usr/local/share/postgresql/extension/  
COPY ./initdb /initdb  
  
RUN chmod go= /initdb \  
&& downloadDir="$(mktemp -d)" \  
&& wget -O "$downloadDir/postgresql.tar.bz2"
"http://ftp.postgresql.org/pub/source/v$PG_VERSION/postgresql-$PG_VERSION.tar.bz2"
\  
&& buildDir="$(mktemp -d)" \  
&& tar --extract --file "$downloadDir/postgresql.tar.bz2" \--directory
"$buildDir" \--strip-components 1 \  
&& rm -rf "$downloadDir" \  
&& apk add --no-cache --virtual .build-deps bison coreutils dpkg-dev dpkg flex
gcc libc-dev libedit-dev libxml2-dev libxslt-dev make libressl-dev perl-utils
perl-ipc-run util-linux-dev zlib-dev openldap-dev \  
&& sed -i 's|#define DEFAULT_PGSOCKET_DIR "/tmp"|#define DEFAULT_PGSOCKET_DIR
"/var/run/postgresql"|g' "$buildDir/src/include/pg_config_manual.h" \  
&& wget -O "$buildDir/config/config.guess"
'http://git.savannah.gnu.org/cgit/config.git/plain/config.guess?id=7d3d27baf8107b630586c962c057e22149653deb'
\  
&& wget -O "$buildDir/config/config.sub"
'http://git.savannah.gnu.org/cgit/config.git/plain/config.sub?id=7d3d27baf8107b630586c962c057e22149653deb'
\  
&& mkdir -p /usr/local/include \  
&& cd "$buildDir" \  
&& ./configure --build="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)"
\--enable-integer-datetimes --enable-thread-safety --enable-tap-tests
--disable-rpath --with-uuid=e2fs --with-gnu-ld --with-pgport=5432
\--prefix=/usr/local --with-includes=/usr/local/include --with-
libraries=/usr/local/lib --with-openssl --with-libxml --with-libxslt --with-
ldap \  
&& make -j "$(nproc)" world \  
&& make install-world \  
&& make -C contrib install \  
&& runDeps="$(scanelf --needed --nobanner --format '%n#p' --recursive
/usr/local | tr ',' '\n' | sort -u | awk 'system("[ -e /usr/local/lib/" $1 "
]") == 0 { next } { print "so:" $1 }' )" \  
&& apk add --no-cache --virtual .postgresql-rundeps $runDeps \  
&& apk del .build-deps \  
&& cd / \  
&& rm -rf "$buildDir" /usr/local/share/doc /usr/local/share/man \  
&& find /usr/local -name '*.a' -delete \  
&& sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!"
/usr/local/share/postgresql/postgresql.conf.sample  
  
ENV VAR_LINUX_USER="postgres" \  
VAR_CONFIG_FILE="$CONFIG_DIR/postgresql.conf" \  
VAR_LOCALE="en_US.UTF-8" \  
VAR_ENCODING="UTF8" \  
VAR_TEXT_SEARCH_CONFIG="english" \  
VAR_HBA="local all all trust, host all all 127.0.0.1/32 trust, host all all
::1/128 trust, host all all all md5" \  
VAR_CREATE_EXTENSION_PGAGENT="yes" \  
VAR_param_data_directory="'/pgdata'" \  
VAR_param_hba_file="'$CONFIG_DIR/pg_hba.conf'" \  
VAR_param_ident_file="'$CONFIG_DIR/pg_ident.conf'" \  
VAR_param_unix_socket_directories="'/var/run/postgresql'" \  
VAR_param_listen_addresses="'*'" \  
VAR_param_timezone="'UTC'" \  
VAR_FINAL_COMMAND="/usr/local/bin/postgres
--config_file=\"\$VAR_CONFIG_FILE\""  
  
USER starter  

