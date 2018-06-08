FROM alpine:latest  
  
ARG BUILD_DATE  
ARG MAKEFLAGS=-j12  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="BitlBee" \  
org.label-schema.description="BitlBee, fully loaded." \  
org.label-schema.url="https://tiuxo.com" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/brianclemens/bitlbee-docker" \  
org.label-schema.vendor="Tiuxo" \  
org.label-schema.schema-version="1.0"  
  
ENV BITLBEE_COMMIT=49ab3cb \  
DISCORD_COMMIT=ae2177a \  
FACEBOOK_COMMIT=553593d \  
HANGOUTS_COMMIT=9d008f2 \  
LINE_COMMIT=156f411 \  
MASTODON_COMMIT=b5a21ed \  
MATRIX_COMMIT=49ea988 \  
MATTERMOST_COMMIT=bc02343 \  
PUSHBULLET_COMMIT=d0898fd \  
ROCKETCHAT_COMMIT=fb8dcc6 \  
SKYPE_COMMIT=cf65095 \  
SLACK_COMMIT=a803b73 \  
STEAM_COMMIT=a6444d2 \  
TELEGRAM_COMMIT=f38ea48 \  
VK_COMMIT=51a91c8 \  
WECHAT_COMMIT=17b15e5 \  
WHATSAPP_COMMIT=81c7285 \  
YAHOO_COMMIT=fbbd9c5 \  
RUNTIME_DEPS=" \  
glib \  
gnutls \  
json-glib \  
libevent \  
libgcrypt \  
libotr \  
libpurple \  
libpurple-bonjour \  
libpurple-oscar \  
libpurple-xmpp \  
openldap \  
protobuf-c"  
  
# bitlbee  
RUN apk add --update --no-cache --virtual build-dependencies \  
build-base \  
git \  
gnutls-dev \  
libevent-dev \  
libotr-dev \  
pidgin-dev \  
openldap-dev; \  
apk add --no-cache --virtual runtime-dependencies ${RUNTIME_DEPS}; \  
cd /root; \  
git clone -n https://github.com/bitlbee/bitlbee; \  
cd bitlbee; \  
git checkout ${BITLBEE_COMMIT}; \  
mkdir /bitlbee-data; \  
./configure --buiild=x86_64-alpine-linux-musl --host=x86_64-alpine-linux-musl
--events=libevent --ldap=1 --otr=plugin --purple=1 --config=/bitlbee-data; \  
make; \  
make install; \  
make install-dev; \  
make install-etc; \  
adduser -u 1000 -S bitlbee; \  
addgroup -g 1000 -S bitlbee; \  
chown -R bitlbee:bitlbee /bitlbee-data; \  
touch /var/run/bitlbee.pid; \  
chown bitlbee:bitlbee /var/run/bitlbee.pid; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# discord  
RUN apk add --no-cache --virtual build-dependencies \  
autoconf \  
automake \  
build-base \  
git \  
glib-dev \  
libtool; \  
cd /root; \  
git clone -n https://github.com/sm00th/bitlbee-discord; \  
cd bitlbee-discord; \  
git checkout ${DISCORD_COMMIT}; \  
./autogen.sh; \  
./configure --build=x86_64-alpine-linux-musl --host=x86_64-alpine-linux-musl;
\  
make; \  
make install; \  
strip /usr/local/lib/bitlbee/discord.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# facebook  
RUN apk add --no-cache --virtual build-dependencies \  
autoconf \  
automake \  
build-base \  
git \  
json-glib-dev \  
libtool; \  
cd /root; \  
git clone -n https://github.com/jgeboski/bitlbee-facebook; \  
cd bitlbee-facebook; \  
git checkout ${FACEBOOK_COMMIT}; \  
./autogen.sh --build=x86_64-alpine-linux-musl --host=x86_64-alpine-linux-musl;
\  
make; \  
make install; \  
strip /usr/local/lib/bitlbee/facebook.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# hangouts  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
json-glib-dev \  
mercurial \  
pidgin-dev \  
protobuf-c-dev; \  
cd /root; \  
hg clone -U https://bitbucket.org/EionRobb/purple-hangouts; \  
cd purple-hangouts; \  
hg update ${HANGOUTS_COMMIT}; \  
make; \  
make install; \  
strip /usr/lib/purple-2/libhangouts.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# naver line  
RUN apk add --no-cache --virtual build-dependencies \  
boost-dev \  
build-base \  
curl \  
flex \  
git \  
libgcrypt-dev \  
libtool \  
openssl-dev \  
pidgin-dev; \  
cd /root; \  
git clone -n https://gitlab.com/bclemens/purple-line; \  
cd purple-line; \  
git checkout ${LINE_COMMIT}; \  
make THRIFT_STATIC=true; \  
make install; \  
strip /usr/lib/purple-2/libline.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# mastodon  
RUN apk add --no-cache --virtual build-dependencies \  
autoconf \  
automake \  
build-base \  
git \  
glib-dev \  
libtool; \  
cd /root; \  
git clone -n https://github.com/kensanata/bitlbee-mastodon; \  
cd bitlbee-mastodon; \  
git checkout ${MASTODON_COMMIT}; \  
./autogen.sh; \  
./configure --build=x86_64-alpine-linux-musl --host=x86_64-alpine-linux-musl;
\  
make; \  
make install; \  
strip /usr/local/lib/bitlbee/mastodon.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# matrix  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
http-parser-dev \  
json-glib-dev \  
git \  
pidgin-dev; \  
cd /root; \  
git clone -n https://github.com/matrix-org/purple-matrix; \  
cd purple-matrix; \  
git checkout ${MATRIX_COMMIT}; \  
make; \  
make install; \  
strip /usr/lib/purple-2/libmatrix.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# mattermost  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
discount-dev \  
git \  
json-glib-dev \  
pidgin-dev; \  
cd /root; \  
git clone -n https://github.com/EionRobb/purple-mattermost; \  
cd purple-mattermost; \  
git checkout ${MATTERMOST_COMMIT}; \  
make; \  
make install; \  
strip /usr/lib/purple-2/libmattermost.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# pushbullet  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
git \  
json-glib-dev \  
pidgin-dev; \  
cd /root; \  
git clone -n https://github.com/EionRobb/pidgin-pushbullet; \  
cd pidgin-pushbullet; \  
git checkout ${PUSHBULLET_COMMIT}; \  
make; \  
make install; \  
strip /usr/lib/purple-2/libpushbullet.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# rocket.chat  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
discount-dev \  
json-glib-dev \  
mercurial \  
pidgin-dev; \  
cd /root; \  
hg clone -U https://bitbucket.org/EionRobb/purple-rocketchat; \  
cd purple-rocketchat; \  
hg update ${ROCKETCHAT_COMMIT}; \  
make; \  
make install; \  
strip /usr/lib/purple-2/librocketchat.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# skype  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
git \  
json-glib-dev \  
pidgin-dev; \  
cd /root; \  
git clone -n https://github.com/EionRobb/skype4pidgin; \  
cd skype4pidgin; \  
git checkout ${SKYPE_COMMIT}; \  
cd skypeweb; \  
make; \  
make install; \  
strip /usr/lib/purple-2/libskypeweb.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# slack  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
git \  
pidgin-dev; \  
cd /root; \  
git clone -n https://github.com/dylex/slack-libpurple; \  
cd slack-libpurple; \  
git checkout ${SLACK_COMMIT}; \  
make; \  
make install; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# steam  
RUN apk add --no-cache --virtual build-dependencies \  
autoconf \  
automake \  
build-base \  
git \  
glib-dev \  
libgcrypt-dev \  
libtool; \  
cd /root; \  
git clone -n https://github.com/bitlbee/bitlbee-steam; \  
cd bitlbee-steam; \  
git checkout ${STEAM_COMMIT}; \  
./autogen.sh --build=x86_64-alpine-linux-musl --host=x86_64-alpine-linux-musl;
\  
make; \  
make install; \  
strip /usr/local/lib/bitlbee/steam.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# telegram  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
git \  
libgcrypt-dev \  
pidgin-dev; \  
cd /root; \  
git clone -n https://github.com/majn/telegram-purple; \  
cd telegram-purple; \  
git checkout ${TELEGRAM_COMMIT}; \  
git submodule update --init --recursive; \  
./configure --build=x86_64-alpine-linux-musl --host=x86_64-alpine-linux-musl
--disable-libwebp; \  
make; \  
make install; \  
strip /usr/lib/purple-2/telegram-purple.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# wechat  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
cargo \  
clang \  
git \  
openssl-dev \  
pidgin-dev; \  
cd /root; \  
git clone -n https://github.com/sbwtw/pidgin-wechat; \  
cd pidgin-wechat; \  
git checkout ${WECHAT_COMMIT}; \  
cargo build --release; \  
cp target/release/libwechat.so /usr/lib/purple-2; \  
strip /usr/lib/purple-2/libwechat.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# vkontakt  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
cmake \  
libtool \  
libxml2-dev \  
mercurial \  
pidgin-dev; \  
cd /root; \  
hg clone -U https://bitbucket.org/olegoandreev/purple-vk-plugin; \  
cd purple-vk-plugin; \  
hg update ${VK_COMMIT}; \  
cd build; \  
cmake ..; \  
make; \  
make install; \  
strip /usr/lib/purple-2/libpurple-vk-plugin.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# whatsapp  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
git \  
pidgin-dev \  
protobuf-dev; \  
cd /root; \  
git clone -n https://github.com/jakibaki/whatsapp-purple; \  
cd whatsapp-purple; \  
git checkout ${WHATSAPP_COMMIT}; \  
make; \  
make install; \  
strip /usr/lib/purple-2/libwhatsapp.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
# yahoo  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
git \  
json-glib-dev \  
pidgin-dev; \  
cd /root; \  
git clone -n https://github.com/EionRobb/funyahoo-plusplus; \  
cd funyahoo-plusplus; \  
git checkout ${YAHOO_COMMIT}; \  
make; \  
make install; \  
strip /usr/lib/purple-2/libyahoo-plusplus.so; \  
rm -rf /root; \  
mkdir /root; \  
apk del --purge build-dependencies  
  
EXPOSE 6697  
VOLUME /bitlbee-data  
  
USER bitlbee  
ENTRYPOINT ["/usr/local/sbin/bitlbee", "-F", "-n", "-d", "/bitlbee-data"]  

