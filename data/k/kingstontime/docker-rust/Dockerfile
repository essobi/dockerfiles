FROM alpine:latest  
MAINTAINER Jonathan Kingston <j@kingston.me>  
  
ENV RUST_DIR rust-1.14.0-x86_64-unknown-linux-gnu  
ENV RUST_PACKAGE $RUST_DIR.tar.gz  
ENV RUST_DOWNLOAD https://static.rust-lang.org/dist/$RUST_PACKAGE  
  
WORKDIR /rust  
  
# Download files and create a layer for perf  
# Do the smaller files first in case they fail  
RUN apk add --no-cache gnupg curl ca-certificates \  
&& curl -fSOL $RUST_DOWNLOAD.asc \  
&& curl -fSOL https://keybase.io/rust/pgp_keys.asc \  
&& curl -fOSL $RUST_DOWNLOAD \  
&& curl -s $RUST_DOWNLOAD.sha256 | sha256sum -c - \  
&& if [ $(gpg pgp_keys.asc | grep 108F66205EAEB0AAA8DD5E1C85AB96E6FA1BE5FE |
wc -l ) != 1 ]; then \  
exit 1; \  
fi \  
&& gpg --import pgp_keys.asc \  
&& if [ $(gpg2 --logger-fd 1 --status-fd 1 --always-trust --with-fingerprint
--verify $RUST_PACKAGE.asc | grep 'Primary key fingerprint' | wc -l) != 1 ];
then \  
exit 2; \  
fi;  
  
# Unpack, housekeeping and install  
# Alpine doesn't support tar --strip-components  
RUN tar -xzvf $RUST_PACKAGE \  
&& mv $RUST_DIR/* . \  
&& rm -rf $RUST_DIR \  
&& rm -f $RUST_PACKAGE \  
&& rm -f $RUST_PACKAGE.asc \  
&& apk del curl \  
&& ./install.sh;  

