FROM alpine:3.6  
LABEL maintainer="L3msh0@gmail.com"  
  
ARG OSAFT_VERSION="17.09.17"  
ARG OSAFT_DIR="/O-Saft"  
ARG
OSAFT_URL="https://github.com/OWASP/O-Saft/archive/${OSAFT_VERSION}.tar.gz"  
ARG
OSAFT_SHA256="18b76650dfca268e32647140a3ef55536dc536182776af62290c916695230ca7"  
  
ARG OPENSSL_VERSION="1.0.2-chacha"  
ARG OPENSSL_DIR="/openssl"  
ARG
OPENSSL_URL="https://github.com/PeterMosmans/openssl/archive/${OPENSSL_VERSION}.tar.gz"  
ARG
OPENSSL_SHA256="ad3d99ec091e403a3a7a678ddda38b392e3204515425827c53dc5baa92d61d67"  
  
ARG NET_SSLEAY_VERSION="1.81"  
ARG NET_SSLEAY_URL="http://search.cpan.org/CPAN/authors/id/M/MI/MIKEM/Net-
SSLeay-${NET_SSLEAY_VERSION}.tar.gz"  
ARG
NET_SSLEAY_SHA256="00cbb6174e628b42178e1445c9fd5a3c5ae2cfd6a5a43e03610ba14786f21b7d"  
ARG NET_SSLEAY_PATCH_FILE="SSLeay.xs.enable_weakssl.diff"  
ARG NET_SSLEAY_PATCH_PATH="/${NET_SSLEAY_PATCH_FILE}"  
ADD ./patch/${NET_SSLEAY_PATCH_FILE} ${NET_SSLEAY_PATCH_PATH}  
  
ENV TERM xterm  
ENV LD_RUN_PATH ${OPENSSL_DIR}/lib  
ENV PATH ${OSAFT_DIR}:${OSAFT_DIR}/contrib:${OPENSSL_DIR}/bin:$PATH  
  
WORKDIR /  
  
# Pull, build and install enhanced openssl  
RUN \  
apk add --upgrade --no-cache \  
ncurses perl perl-readonly perl-net-dns perl-io-socket-ssl krb5-libs openssl
ca-certificates && \  
update-ca-certificates && \  
\  
# pull and extract module  
wget $OPENSSL_URL -O /tmp/openssl.tar.gz && \  
\  
# check sha256 if there is one  
[ -n "$OPENSSL_SHA256" ] && \  
echo "$OPENSSL_SHA256 /tmp/openssl.tar.gz" | sha256sum -c ; \  
\  
tar -xzf /tmp/openssl.tar.gz -C /tmp && \  
\  
cd /tmp/openssl-* && \  
\  
# build openssl {  
# install development tools  
apk add --upgrade --no-cache --virtual .builddeps alpine-sdk linux-headers
gmp-dev lksctp-tools-dev krb5-dev zlib-dev perl-dev && \  
\  
# patch openssl.cnf for GOST  
sed -i '/RANDFILE/a openssl_conf=openssl_def' apps/openssl.cnf && \  
# using echo instead of cat to avoid problems with stacked commands:  
# cat -> shell -> docker  
(\  
echo 'openssl_conf=openssl_def'; \  
echo '[openssl_def]'; \  
echo 'engines=engine_section'; \  
echo '[engine_section]'; \  
echo 'gost=gost_section'; \  
echo '[gost_section]'; \  
echo 'engine_id = gost'; \  
echo 'default_algorithms=ALL'; \  
echo 'CRYPT_PARAMS=id-Gost28147-89-CryptoPro-A-ParamSet'; \  
) >> apps/openssl.cnf && \  
# config with all options, even if they are default  
LDFLAGS="-rpath=$LD_RUN_PATH" && export LDFLAGS && \  
# see description for LDFLAGS above  
./config --prefix=$OPENSSL_DIR \--openssldir=$OPENSSL_DIR/ssl \  
\--shared \  
\--with-krb5-flavor=MIT --with-krb5-dir=/usr/include/krb5/ \  
-fPIC zlib zlib-dynamic enable-zlib enable-npn sctp \  
enable-deprecated enable-weak-ssl-ciphers \  
enable-heartbeats enable-unit-test enable-ssl-trace \  
enable-ssl3 enable-ssl3-method enable-ssl2 \  
enable-tls1 enable-tls1-method enable-tls \  
enable-tls1-1 enable-tls1-1-method enable-tlsext \  
enable-tls1-2 enable-tls1-2-method enable-tls1-2-client \  
enable-dtls1 enable-dtls1-method \  
enable-dtls1-2 enable-dtls1-2-method \  
enable-md2 enable-md4 enable-mdc2 \  
enable-rc2 enable-rc4 enable-rc5 \  
enable-sha0 enable-sha1 enable-sha256 enable-sha512 \  
enable-aes enable-cms enable-dh enable-egd \  
enable-des enable-dsa enable-rsa enable-rsax \  
enable-ec enable-ec2m enable-ecdh enable-ecdsa \  
enable-blake2 enable-bf enable-cast enable-camellia \  
enable-gmp enable-gost enable-GOST enable-idea \  
enable-poly1305 enable-krb5 enable-rdrand enable-rmd160 \  
enable-seed enable-srp enable-whirlpool \  
enable-rfc3779 enable-ec_nistp_64_gcc_128 experimental-jpake \  
-DOPENSSL_USE_BUILD_DATE -DTLS1_ALLOW_EXPERIMENTAL_CIPHERSUITES -DTEMP_GOST_TLS \  
&& \  
make depend && make && make report -i && make install && \  
# make report most likely fails, hence -i  
# simple test  
echo -n "# number of ciphers $OPENSSL_DIR/bin/openssl: " && \  
$OPENSSL_DIR/bin/openssl ciphers -V ALL:COMPLEMENTOFALL:aNULL|wc -l && \  
# cleanup  
# build openssl }  
\  
cd / && \  
rm -rf /tmp/openssl* && \  
# Installing Net::SSLeay  
wget $NET_SSLEAY_URL -O /tmp/Net-SSLeay.tar.gz && \  
# check sha256 if there is one  
[ -n "$NET_SSLEAY_SHA256" ] && \  
echo "$NET_SSLEAY_SHA256 /tmp/Net-SSLeay.tar.gz" | sha256sum -c ; \  
tar -xzf /tmp/Net-SSLeay.tar.gz -C /tmp && \  
cd /tmp/Net-SSLeay-* && \  
patch < ${NET_SSLEAY_PATCH_PATH} && \  
env OPENSSL_PREFIX=/openssl perl Makefile.PL PREFIX=/usr/local INC="-I
/openssl/include" DEFINE=-DOPENSSL_BUILD_UNSAFE=1 && \  
make && \  
make install && \  
rm -rf /tmp/Net-SSLeay* ${NET_SSLEAY_PATCH_PATH} && \  
\  
# cleanup  
apk del --purge .builddeps openssl && \  
\  
# Pull and install O-Saft  
cd / && \  
mkdir $OSAFT_DIR && \  
adduser -D -h ${OSAFT_DIR} osaft && \  
\  
wget $OSAFT_URL -O /tmp/osaft.tar.gz && \  
# check sha256 if there is one  
[ -n "$OSAFT_SHA256" ] && \  
echo "$OSAFT_SHA256 /tmp/osaft.tar.gz" | sha256sum -c ; \  
\  
tar -xzf /tmp/osaft.tar.gz --strip-components=1 -C $OSAFT_DIR && \  
chown -R root:root $OSAFT_DIR && \  
chown -R osaft:osaft $OSAFT_DIR/contrib && \  
chown osaft:osaft $OSAFT_DIR/.o-saft.pl && \  
mv $OSAFT_DIR/.o-saft.pl $OSAFT_DIR/.o-saft.pl-orig && \  
sed \  
-e "s:^#--openssl=.*:--openssl=$OPENSSL_DIR/bin/openssl:" \  
-e "s:^#--ca-path:--ca-path:" \  
< $OSAFT_DIR/.o-saft.pl-orig \  
> $OSAFT_DIR/.o-saft.pl && \  
chmod 666 $OSAFT_DIR/.o-saft.pl && \  
rm -f /tmp/osaft.tar.gz  
  
WORKDIR $OSAFT_DIR  
USER osaft  
  
ENTRYPOINT ["perl", "./o-saft.pl"]  
CMD ["--norc", "--help"]  

