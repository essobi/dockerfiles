FROM alpine:3.5  
ENV LANG en_US.utf8  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
  
ENV PG_MAJOR 9.6  
ENV PG_VERSION 9.6.1  
ENV PG_SHA256 e5101e0a49141fc12a7018c6dad594694d3a3325f5ab71e93e0e51bd94e51fcd  
  
RUN set -ex \  
\  
&& apk add --no-cache --virtual .fetch-deps \  
ca-certificates \  
openssl \  
tar \  
\  
&& wget -O postgresql.tar.bz2
"https://ftp.postgresql.org/pub/source/v$PG_VERSION/postgresql-$PG_VERSION.tar.bz2"
\  
&& echo "$PG_SHA256 *postgresql.tar.bz2" | sha256sum -c - \  
&& mkdir -p /usr/src/postgresql \  
&& tar \  
\--extract \  
\--file postgresql.tar.bz2 \  
\--directory /usr/src/postgresql \  
\--strip-components 1 \  
&& rm postgresql.tar.bz2 \  
\  
&& apk add --no-cache --virtual .build-deps \  
bison \  
flex \  
gcc \  
# krb5-dev \  
libc-dev \  
libedit-dev \  
libxml2-dev \  
libxslt-dev \  
make \  
# openldap-dev \  
openssl-dev \  
perl \  
# perl-dev \  
# python-dev \  
# python3-dev \  
# tcl-dev \  
util-linux-dev \  
zlib-dev \  
\  
&& cd /usr/src/postgresql \  
# configure options taken from:  
# https://anonscm.debian.org/cgit/pkg-
postgresql/postgresql.git/tree/debian/rules?h=9.5  
&& ./configure \  
# "/usr/src/postgresql/src/backend/access/common/tupconvert.c:105: undefined
reference to `libintl_gettext'"  
# --enable-nls \  
\--enable-integer-datetimes \  
\--enable-thread-safety \  
\--enable-tap-tests \  
# skip debugging info -- we want tiny size instead  
# --enable-debug \  
\--disable-rpath \  
\--with-uuid=e2fs \  
\--with-gnu-ld \  
\--with-pgport=5432 \  
\--with-system-tzdata=/usr/share/zoneinfo \  
\--prefix=/usr/local \  
\  
\--with-openssl \  
\--with-libxml \  
\--with-libxslt \  
&& make -j "$(getconf _NPROCESSORS_ONLN)" world \  
&& make install-world \  
&& make -C contrib install \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add \--no-cache --virtual .postgresql-rundeps \  
$runDeps \  
bash \  
su-exec \  
tzdata \  
&& apk del .fetch-deps .build-deps \  
&& cd / \  
&& rm -rf \  
/usr/src/postgresql \  
/usr/local/include/* \  
/usr/local/share/doc \  
/usr/local/share/man \  
&& find /usr/local -name '*.a' -delete  
  
# make the sample config easier to munge (and "correct by default")  
RUN sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!"
/usr/local/share/postgresql/postgresql.conf.sample  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql  
  
ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH  
RUN apk add musl  
RUN apk add --update libbz2 libcrypto1.0 expat libffi gdbm ncurses-libs
readline sqlite-libs libssl1.0 zlib  
RUN apk add python  
RUN apk --no-cache add openssl  
RUN apk --no-cache add --virtual ca-certificates  
#RUN wget https://bootstrap.pypa.io/get-pip.py  
#RUN python get-pip.py  
#RUN rm get-pip.py  
RUN apk --no-cache add python postgresql-libs && \  
apk --no-cache add --virtual build-dependencies python-dev gcc musl-dev
postgresql-dev wget  
# wget -q
https://ftp.postgresql.org/pub/pgadmin3/pgadmin4/v1.1/pip/pgadmin4-1.1-py2-none-
any.whl && \  
# pip --no-cache-dir install pgadmin4-1.1-py2-none-any.whl && \  
# rm pgadmin4-1.1-py2-none-any.whl && \  
# apk del build-dependencies  
#ENV PACKAGE_DIR /usr/lib/python2.7/site-packages/pgadmin4  
#ENV CONFIG_FILE $PACKAGE_DIR/config_local.py  
#RUN touch $CONFIG_FILE && \  
# echo "SERVER_MODE = False" >> $CONFIG_FILE && \  
# echo "DEFAULT_SERVER = '0.0.0.0'" >> $CONFIG_FILE && \  
# adduser -D pgadmin  
RUN apk add postgresql-contrib  
  
ADD version.json /opt  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 5432  

