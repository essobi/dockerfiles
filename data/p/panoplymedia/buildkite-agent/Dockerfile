FROM buildkite/agent:3  
MAINTAINER Jason Cox <jason.cox@panoply.fm>  
  
ADD VERSION .  
  
# POSTGRES SETUP  
# --------------  
RUN set -ex; \  
postgresHome="$(getent passwd postgres)"; \  
postgresHome="$(echo "$postgresHome" | cut -d: -f6)"; \  
[ "$postgresHome" = '/var/lib/postgresql' ]; \  
mkdir -p "$postgresHome"; \  
chown -R postgres:postgres "$postgresHome"  
  
# su-exec (gosu-compatible) is installed further down  
# make the "en_US.UTF-8" locale so postgres will be utf-8 enabled by default  
# alpine doesn't require explicit locale-file generation  
ENV LANG en_US.utf8  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
ENV PG_MAJOR 10  
ENV PG_VERSION 10.4  
ENV PG_SHA256 1b60812310bd5756c62d93a9f93de8c28ea63b0df254f428cd1cf1a4d9020048  
  
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
coreutils \  
dpkg-dev dpkg \  
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
# configure: error: prove not found  
perl-utils \  
# configure: error: Perl module IPC::Run is required to run TAP tests  
perl-ipc-run \  
# perl-dev \  
# python-dev \  
# python3-dev \  
# tcl-dev \  
util-linux-dev \  
zlib-dev \  
\  
&& cd /usr/src/postgresql \  
# update "DEFAULT_PGSOCKET_DIR" to "/var/run/postgresql" (matching Debian)  
# see https://anonscm.debian.org/git/pkg-
postgresql/postgresql.git/tree/debian/patches/51-default-sockets-in-
var.patch?id=8b539fcb3e093a521c095e70bdfa76887217b89f  
&& awk '$1 == "#define" && $2 == "DEFAULT_PGSOCKET_DIR" && $3 == "\"/tmp\"" {
$3 = "\"/var/run/postgresql\""; print; next } { print }'
src/include/pg_config_manual.h > src/include/pg_config_manual.h.new \  
&& grep '/var/run/postgresql' src/include/pg_config_manual.h.new \  
&& mv src/include/pg_config_manual.h.new src/include/pg_config_manual.h \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
# explicitly update autoconf config.guess and config.sub so they support more
arches/libcs  
&& wget -O config/config.guess
'https://git.savannah.gnu.org/cgit/config.git/plain/config.guess?id=7d3d27baf8107b630586c962c057e22149653deb'
\  
&& wget -O config/config.sub
'https://git.savannah.gnu.org/cgit/config.git/plain/config.sub?id=7d3d27baf8107b630586c962c057e22149653deb'
\  
# configure options taken from:  
# https://anonscm.debian.org/cgit/pkg-
postgresql/postgresql.git/tree/debian/rules?h=9.5  
&& ./configure \  
\--build="$gnuArch" \  
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
\--with-includes=/usr/local/include \  
\--with-libraries=/usr/local/lib \  
\  
# these make our image abnormally large (at least 100MB larger), which seems
uncouth for an "Alpine" (ie, "small") variant :)  
# --with-krb5 \  
# --with-gssapi \  
# --with-ldap \  
# --with-tcl \  
# --with-perl \  
# --with-python \  
# --with-pam \  
\--with-openssl \  
\--with-libxml \  
\--with-libxslt \  
&& make -j "$(nproc)" world \  
&& make install-world \  
&& make -C contrib install \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add \--no-cache --virtual .postgresql-rundeps \  
$runDeps \  
bash \  
su-exec \  
# tzdata is optional, but only adds around 1Mb to image size and is
recommended by Django documentation:  
# https://docs.djangoproject.com/en/1.10/ref/databases/#optimizing-postgresql-
s-configuration  
tzdata \  
&& apk del .fetch-deps .build-deps \  
&& cd / \  
&& rm -rf \  
/usr/src/postgresql \  
/usr/local/share/doc \  
/usr/local/share/man \  
&& find /usr/local -name '*.a' -delete  
  
# make the sample config easier to munge (and "correct by default")  
RUN sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!"
/usr/local/share/postgresql/postgresql.conf.sample  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres:postgres
/var/run/postgresql && chmod 2777 /var/run/postgresql  
  
ENV PGDATA /var/lib/postgresql/data  
RUN mkdir -p "$PGDATA" && chown -R postgres:postgres "$PGDATA" && chmod 777
"$PGDATA" # this 777 will be replaced by 700 at runtime (allows semi-arbitrary
"--user" values)  
VOLUME /var/lib/postgresql/data  
# --------------  
# CITUS SETUP  
# -----------  
ARG VERSION=7.4.0  
RUN apk add --no-cache \  
\--virtual builddeps \  
build-base \  
curl \  
curl-dev \  
openssl-dev && \  
apk add --no-cache libcurl && \  
curl -sfLO "https://github.com/citusdata/citus/archive/v${VERSION}.tar.gz" &&
\  
tar xzf "v${VERSION}.tar.gz" && \  
cd "citus-${VERSION}" && \  
./configure && \  
make install && \  
cd .. && \  
rm -rf "citus-${VERSION}" "v${VERSION}.tar.gz" && \  
apk del builddeps  
  
# add citus to default PostgreSQL config  
RUN echo "shared_preload_libraries='citus'" >>
/usr/local/share/postgresql/postgresql.conf.sample  
# -----------  
# ruby  
# -----------  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
ENV RUBY_VERSION 2.3.3  
ENV RUBYGEMS_VERSION 2.6.10  
RUN set -ex \  
&& apk add --no-cache \  
autoconf \  
bash \  
bison \  
bzip2 \  
bzip2-dev \  
ca-certificates \  
coreutils \  
curl \  
gcc \  
git \  
gdbm-dev \  
glib-dev \  
libc-dev \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
make \  
ncurses-dev \  
openssl-dev \  
procps \  
readline-dev \  
yaml-dev \  
zlib-dev \  
redis \  
ruby \  
ruby-dev  
  
ENV PATH /usr/local/rbenv/shims:/usr/local/rbenv/bin:$PATH  
ENV RBENV_ROOT /usr/local/rbenv  
ENV CONFIGURE_OPTS="ac_cv_func_isnan=yes ac_cv_func_isinf=yes --disable-
install-doc"  
RUN git clone \--depth 1 git://github.com/sstephenson/rbenv.git ${RBENV_ROOT}
\  
&& git clone \--depth 1 https://github.com/sstephenson/ruby-build.git
${RBENV_ROOT}/plugins/ruby-build \  
&& git clone \--depth 1 git://github.com/jf/rbenv-gemset.git
${RBENV_ROOT}/plugins/rbenv-gemset \  
&& ${RBENV_ROOT}/plugins/ruby-build/install.sh  
  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh  
  
RUN rbenv install $RUBY_VERSION && \  
rbenv global $RUBY_VERSION  
  
RUN gem install bundler  
  
# faster nokogiri installs  
RUN bundle config build.nokogiri --use-system-libraries  
  
# Install globally, don't create ".bundle" in all our apps  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  
# -----------  
# node  
# ----------  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
binutils-gold \  
curl \  
g++ \  
gcc \  
gnupg \  
libgcc \  
linux-headers \  
make \  
python \  
libstdc++ \  
ncurses \  
ca-certificates \  
openssl \  
coreutils \  
python2 \  
grep \  
util-linux \  
binutils \  
findutils  
  
# nvm node version manager  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh |
/bin/bash  
ENV NVM_DIR /root/.nvm  
RUN [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \  
nvm install -s 9.11 && nvm use 9.11  
RUN [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \  
npm install -g yarn  
RUN echo "source $NVM_DIR/nvm.sh" >> /etc/profile.d/nvm.sh  
RUN echo "source $NVM_DIR/nvm.sh" >> $HOME/.bashrc  
# ----------  
# golang  
# ----------  
ENV GOLANG_VERSION 1.9.4  
RUN set -eux; \  
apk add --no-cache --virtual .build-deps \  
bash \  
gcc \  
musl-dev \  
openssl \  
go  
  
ENV GOROOT_BOOTSTRAP=/usr/lib/go GOOS=linux GOARCH=amd64 GOHOSTOS=linux
GOHOSTARCH=amd64 GO386=387  
ENV GOPATH $HOME/go  
ENV PATH $GOPATH/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
  
RUN ["/bin/bash", "-c", "bash < <(curl -s -S -L
https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-
installer)"]  
RUN ["/bin/bash", "-c", "source /root/.gvm/scripts/gvm && gvm install go1.10
&& gvm use go1.10"]  
RUN echo "source /root/.gvm/scripts/gvm" >> /etc/profile.d/gvm.sh  
RUN echo "source /root/.gvm/scripts/gvm" >> $HOME/.bashrc  
  
# install dep  
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh  
# ----------  
# set up phantomjs  
RUN apk update && apk add --no-cache fontconfig && \  
wget -qO-
"https://github.com/dustinblackman/phantomized/releases/download/2.1.1a/dockerized-
phantomjs.tar.gz" | tar xz -C / && \  
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \  
npm config set user 0 && \  
npm install -g phantomjs-prebuilt  
  
RUN apk add --update -X http://dl-cdn.alpinelinux.org/alpine/edge/testing
chromaprint-dev  
RUN apk add --no-cache tini sudo chromaprint  
  
# add build scripts  
Add scripts/init_db /scripts/init_db  
RUN chmod +x /scripts/init_db  
  
# setup postgres  
USER postgres  
RUN /bin/bash /scripts/init_db  
  
USER root  
  
# allow ssh config  
RUN curl -fL "https://raw.githubusercontent.com/buildkite/docker-ssh-env-
config/d06f20bdc7457a647bfe3724d94525f83c863091/ssh-env-config.sh" -o
/usr/local/bin/ssh-env-config.sh \  
&& chmod +x /usr/local/bin/ssh-env-config.sh  
  
RUN rm /scripts/init_db  
  
ADD init.sh /usr/local/bin/init.sh  
RUN chmod +x /usr/local/bin/init.sh  
ENTRYPOINT ["/sbin/tini", "--", "init.sh"]  
CMD ["start"]  

