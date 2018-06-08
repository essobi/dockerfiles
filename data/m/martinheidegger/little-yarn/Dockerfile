FROM alpine:3.4  
  
WORKDIR /usr/src/app  
  
ENV BUNDLE_PATH=/usr/local/bundle  
  
# NOTE: libxml2-dev libxslt-dev for nokogiri (actionview 4.2 <\- rails-html-
sanitizer)  
# NOTE: libffi-dev for ffi. see
https://github.com/ffi/ffi/issues/485#issuecomment-191382158  
# NOTE: gcc, g++ and libc-dev for json gem  
# NOTE: linux-headers for raindrops gem  
# NOTE: bash for ci  
RUN mkdir -p /usr/src/app \  
&& apk update \  
&& apk add --no-cache make bash gcc g++ man linux-headers curl git openssl
openssh-client \  
python binutils-gold linux-headers gnupg libgcc \  
## For the build of node  
&& curl -sL https://raw.githubusercontent.com/martinheidegger/install-
node/master/install_node.sh | \  
NODE_VERSION="v6.10.1" \  
NODE_VARIANT="make" \  
bash \  
&& rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/perl* /usr/share/man
|| true  

