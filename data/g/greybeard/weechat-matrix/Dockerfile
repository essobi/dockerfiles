FROM alpine  
  
ENV TERM=screen-256color  
ENV LANG=C.UTF-8  
ENV UID=1000  
ENV GID=1000  
  
ADD run.sh /  
  
RUN BUILD_DEPS=" \  
build-base \  
ca-certificates \  
cmake \  
curl-dev \  
gnutls-dev \  
jq \  
libcurl \  
libgcrypt-dev \  
libintl \  
lua-dev \  
ncurses-dev \  
perl-dev \  
python2-dev \  
tar \  
zlib-dev" \  
&& apk -U upgrade && apk add \  
${BUILD_DEPS} \  
curl \  
gnutls \  
libgcrypt \  
lua \  
lua-cjson \  
ncurses \  
perl \  
python \  
shadow \  
su-exec \  
&& update-ca-certificates \  
&& WEECHAT_TARBALL="$(curl -sS
https://api.github.com/repos/weechat/weechat/releases/latest | jq .tarball_url
-r)" \  
&& curl -sSL $WEECHAT_TARBALL -o /tmp/weechat.tar.gz \  
&& mkdir -p /tmp/weechat/build \  
&& tar xzf /tmp/weechat.tar.gz --strip 1 -C /tmp/weechat \  
&& cd /tmp/weechat/build \  
&& cmake .. -DCMAKE_INSTALL_PREFIX=/usr \  
&& make && make install \  
&& mkdir -p /weechat/.weechat/lua/autoload \  
&& addgroup -g $GID -S weechat \  
&& adduser -u $UID -D -S -h /weechat -s /sbin/nologin -G weechat weechat \  
&& curl -sSL https://raw.githubusercontent.com/torhve/weechat-matrix-protocol-
script/master/matrix.lua -o /weechat/.weechat/lua/matrix.lua \  
&& ln -s /weechat/.weechat/lua/matrix.lua /weechat/.weechat/lua/autoload/ \  
&& apk del ${BUILD_DEPS} \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/*  
  
EXPOSE 9001  
  
ENTRYPOINT ["/run.sh"]  
CMD ["--dir /weechat"]  
  

