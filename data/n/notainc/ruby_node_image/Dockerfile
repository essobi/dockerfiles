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
&& apk add --no-cache make bash ruby ruby-io-console ruby-dev ruby-bigdecimal
ruby-irb \  
gcc g++ man linux-headers libffi-dev libxml2-dev libxslt-dev curl git \  
## For the build of node  
&& apk add \--no-cache python binutils-gold linux-headers gnupg libgcc \  
&& curl -sL https://raw.githubusercontent.com/martinheidegger/install-
node/master/install_node.sh | \  
NODE_VERSION="v5.1.0" \  
YARN_VERSION="v0.20.3" \  
NODE_VARIANT="make" \  
bash \  
&& gem install bundler --no-doc \  
&& rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/perl* /usr/share/man
|| true  
  
ADD entrypoint.sh /  
  
ENTRYPOINT ["/bin/bash", "-l", "/entrypoint.sh"]  
  
ONBUILD ADD package.json yarn.lock ./  
ONBUILD RUN yarn install --no-emoji --ignore-optional --strict-semver
--network-concurrency=15 --no-cache  
  
ONBUILD ADD Gemfile* ./  
ONBUILD RUN bundle install --jobs 4 --retry 3 --deployment --without test
development cap machine \  
&& rm -r vendor/bundle/ruby/*/cache  

