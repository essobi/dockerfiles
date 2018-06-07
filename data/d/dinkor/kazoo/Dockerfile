FROM alpine:3.5  
MAINTAINER Sergey Korobkov <skorobkov@dinkor.net>  
  
ARG KAZOO_REPO=https://github.com/2600hz/kazoo.git  
ARG KAZOO_BRANCH=master  
ARG USER=kazoo  
ARG ERLANG_VERSION=18.3  
ARG KAZOO_DIR=/opt/kazoo  
ARG KERL_CONFIGURE_OPTIONS="--without-javac --without-odbc"  
ARG HTMLDOC_VERSION=1.8.29  
  
COPY kazoo_* /usr/local/sbin/  
  
RUN apk update \  
&& apk add \  
bash \  
build-base \  
curl \  
dumb-init \  
expat \  
expat-dev \  
git \  
grep \  
#libxslt \  
#libxslt-dev \  
libstdc++ \  
ncurses-libs \  
ncurses-dev \  
perl \  
openssl \  
openssl-dev \  
python \  
&& curl -fSL -o /tmp/kerl
https://raw.githubusercontent.com/kerl/kerl/master/kerl \  
&& chmod +x /tmp/kerl \  
&& /tmp/kerl update releases \  
&& /tmp/kerl build ${ERLANG_VERSION} ${ERLANG_VERSION} \  
&& /tmp/kerl install ${ERLANG_VERSION} /tmp/erlang \  
&& /tmp/kerl cleanup all \  
&& export PATH=/tmp/erlang/bin:${PATH} \  
  
&& curl -fSL -o /tmp/htmldoc.tar.gz
https://www.msweet.org/files/project1/htmldoc-${HTMLDOC_VERSION}-source.tar.gz
\  
&& mkdir /tmp/htmldoc_build \  
&& tar -xzf /tmp/htmldoc.tar.gz --strip-components=1 -C /tmp/htmldoc_build \  
&& cd /tmp/htmldoc_build \  
&& ./configure --prefix=/usr --without-gui \  
&& make install \  
&& git clone --depth 1 --single-branch -b ${KAZOO_BRANCH} ${KAZOO_REPO}
/tmp/kazoo_build \  
&& make -C /tmp/kazoo_build deps compile build-release \  
  
&& mkdir -p ${KAZOO_DIR} \  
&& adduser -D -h ${KAZOO_DIR} -s /bin/false ${USER} ${USER} \  
&& mv /tmp/kazoo_build/_rel/kazoo/* ${KAZOO_DIR} \  
&& chown -R ${USER}:${USER} ${KAZOO_DIR} \  
&& chmod +x /usr/local/sbin/kazoo_* \  
&& apk del --purge \  
build-base \  
curl \  
expat-dev \  
git \  
grep \  
#libxslt-dev \  
ncurses-dev \  
perl \  
openssl-dev \  
python \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf ~/.kerl/ \  
&& rm -rf /tmp/*  
  
USER ${USER}  
WORKDIR ${KAZOO_DIR}  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["kazoo_start"]  

