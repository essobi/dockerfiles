FROM alpine:3.5  
  
RUN set -ex \  
&& apk update \  
&& apk add \  
autoconf \  
bison \  
bzip2 \  
bzip2-dev \  
ca-certificates \  
coreutils \  
dpkg-dev dpkg \  
gcc \  
gdbm-dev \  
glib-dev \  
libc-dev \  
libffi-dev \  
openssl \  
libressl-dev \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
make \  
ncurses-dev \  
procps \  
readline-dev \  
ruby \  
tar \  
xz \  
yaml-dev \  
zlib-dev \  
postgresql-dev \  
sqlite-dev \  
imagemagick-dev \  
git \  
bash \  
tzdata \  
nodejs  
  
RUN adduser -D luser  
ARG HOMEDIR=/home/luser  
USER luser  
WORKDIR $HOMEDIR  
  
# Never install Rdoc/RI  
RUN { \  
echo 'install: --no-document' ; \  
echo 'update: --no-document' ; \  
} >> ~/.gemrc  
  
# Intall rbenv + ruby-build  
RUN set -ex \  
&& git clone https://github.com/rbenv/rbenv.git ~/.rbenv \  
&& mkdir -p ~/.rbenv/plugins \  
&& git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-
build  
  
# Install rubies  
ENV
PATH=${HOMEDIR}/.rbenv/bin:${HOMEDIR}/.rbenv/shims:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ARG RUBIES="2.2.6 2.2.7 2.3.3 2.3.4 2.4.0 2.4.1"  
RUN set -ex ; \  
for version in $RUBIES ; do \  
rbenv install $version ; \  
rbenv local $version ; \  
gem install bundler ; \  
done ; \  
rbenv local --unset ;  
  
CMD ["bash"]  

