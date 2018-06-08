FROM debian:jessie  
ENV DEBIAN_FRONTEND=noninteractive LANG=es_ES.UTF-8 LANGUAGE=es_ES.UTF-8
LC_ALL=es_ES.UTF-8 \  
XDG_DATA_HOME="/var/lib/trytond/.local/share" \  
TRYTON_HOME="/var/lib/trytond"  
  
  
RUN sed -i 's/main$/main contrib non-free/g' /etc/apt/sources.list \  
&& useradd -d $TRYTON_HOME tryton && mkdir -p $XDG_DATA_HOME $TRYTON_HOME/.ssh
/var/run/sshd \  
&& chown -R tryton $TRYTON_HOME $XDG_DATA_HOME \  
&& apt-get update && apt-get install -y --no-install-recommends locales ca-
certificates wget \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& echo $LANG UTF-8 >> /etc/locale.gen \  
&& locale-gen \  
&& apt-get install -y --no-install-recommends dash libyaml-dev freetds-dev \  
libldap2-dev libsasl2-dev libpq-dev autoconf libtool automake \  
libmariadb-client-lgpl-dev-compat libmariadb-client-lgpl-dev libmariadbd-dev \  
sqlite sqlite3 libsqlite3-dev libmagic-dev \  
libxml2-dev libxslt-dev libjpeg-dev mercurial git build-essential libreadline-
dev \  
gcc libffi-dev libncurses5-dev ttf-mscorefonts-installer rabbitmq-server \  
&& rm -rf /var/cache/apt/* /var/lib/apt/* /var/tmp/* /tmp/* /var/log/*
/usr/share/doc/* /usr/share/man/* /root/.npm || true  
  
RUN apt-get update && wget -O - https://deb.nodesource.com/setup_6.x | bash -
\  
&& apt-get install -y --no-install-recommends nodejs \  
&& npm install -g grunt bower gulp yarn \  
&& rm -rf /var/cache/apt/* /var/lib/apt/* /var/tmp/* /tmp/* /var/log/*
/usr/share/doc/* /usr/share/man/* /root/.npm || true  
  
RUN ln -s /usr/bin/mariadb_config /usr/bin/mysql_config || true  
RUN ln -s /usr/bin/nodejs /usr/bin/node || true  
  
ENV TINI_VERSION v0.14.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "-g","--"]  
  
ENV SASSC_VERSION=3.4.2 LIBSASS_VERSION=3.4.4  
RUN wget -O - https://github.com/sass/libsass/archive/$LIBSASS_VERSION.tar.gz
| tar -zvxf- -C /tmp \  
&& wget -O - https://github.com/sass/sassc/archive/$SASSC_VERSION.tar.gz | tar
-zvxf- -C /tmp \  
&& cd /tmp/libsass-$LIBSASS_VERSION && autoreconf --force --install &&
./configure --enable-shared --prefix=/usr/local \  
&& cd /tmp/sassc-$SASSC_VERSION &&
SASS_LIBSASS_PATH=/tmp/libsass-$LIBSASS_VERSION && make -j5 && make install \  
&& cd libsass-$LIBSASS_VERSION && make install \  
&& rm -rf /var/cache/apt/* /var/lib/apt/* /var/tmp/* /tmp/* /var/log/*
/usr/share/doc/* /usr/share/man/* /root/.npm || true  
  
RUN apt-get update && apt-get install -y --no-install-recommends python-uno
python-stdnum \  
python-support python-cairo python-pil python-dev python-virtualenv virtualenv
python-pip \  
&& rm -rf /var/cache/apt/* /var/lib/apt/* /var/tmp/* /tmp/* /var/log/*
/usr/share/doc/* /usr/share/man/* /root/.npm || true  
  
RUN apt-get update && apt-get install -y --no-install-recommends libreoffice-
writer \  
&& rm -rf /var/cache/apt/* /var/lib/apt/* /var/tmp/* /tmp/* /var/log/*
/usr/share/doc/* /usr/share/man/* /root/.npm || true  
  
  
  
  
  
WORKDIR /app  
COPY bashrc /root/.bashrc  
COPY unoconv /usr/local/bin  
  
ENV TRYTON_VERSION=4.0 \  
ENVIRONMENT="dev" \  
PYTHON_BIN="/app/.env/bin/python" \  
TRYTOND_BIN="trytond/bin/trytond" \  
TRYTOND_CONFIG="trytond.conf" \  
TRYTOND_LOGCONFIG="trytond-log.conf" \  
TRYTOND_ARGS="" \  
DB_NAME="" \  
TRYTOND_DATABASE_URI="postgresql://tryton:tryton@postgres:5432/"  
#CMD ["sshd","-e","-D"]  
#CMD ["su","tryton","-p","-c", "${PYTHON_BIN} ${TRYTOND_BIN} -c
${TRYTOND_CONFIG} --logconf ${TRYTOND_LOGCONFIG} -v"]  
USER tryton  
CMD ["/bin/dash","-c","${PYTHON_BIN} ${TRYTOND_BIN} -c ${TRYTOND_CONFIG}
--logconf ${TRYTOND_LOGCONFIG} -v"]  

