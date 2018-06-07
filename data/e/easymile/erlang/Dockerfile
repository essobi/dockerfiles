FROM alpine:3.7  
  
MAINTAINER frederic.cabestre [at] easymile.com  
  
ENV PATH="/usr/local/asdf/bin:/usr/local/asdf/shims:$PATH" \  
ASDF_ERLANG_VERSION=20.2.2  
  
WORKDIR /usr/local  
  
RUN apk add \--no-cache --update \  
# Erlang Build dependencies, removed in the end  
autoconf=2.69-r0 \  
bash=4.4.12-r2 \  
curl=7.57.0-r0 \  
dpkg-dev=1.18.24-r0 \  
g++=6.4.0-r5 \  
gcc=6.4.0-r5 \  
git=2.15.0-r1 \  
libssh-dev=0.7.5-r2 \  
make=4.2.1-r0 \  
ncurses-dev=6.0_p20170930-r0 \  
openssl-dev=1.0.2n-r0 \  
  
# Runtime dependencies  
libcrypto1.0=1.0.2n-r0 \  
openssh-client=7.5_p1-r8 && \  
  
git clone https://github.com/asdf-vm/asdf.git /usr/local/asdf --branch v0.2.0
&& \  
asdf plugin-add erlang https://github.com/asdf-vm/asdf-erlang.git && \  
asdf install erlang "$ASDF_ERLANG_VERSION" && \  
  
apk del --no-cache dpkg-dev autoconf libssh-dev openssl-dev ncurses-dev && \  
rm -rf /var/cache/apk/*  

