FROM cloudgear/build-deps:14.04  
MAINTAINER Alexander Bobrov, ITBeaver <al.bobrov@itbeaver.co>  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV RUBY_VERSION 2.3  
ENV NODE_VERSION 4.5.0  
  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done && \  
  
  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C3173AA6 &&
\  
echo deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu trusty main >
/etc/apt/sources.list.d/brightbox-ruby-ng-trusty.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 16932B16 &&
\  
echo deb http://ppa.launchpad.net/builds/sphinxsearch-rel22/ubuntu trusty main
> /etc/apt/sources.list.d/sphinxsearch-trusty.list && \  
apt-get update -q && apt-get install -yq --no-install-recommends \  
ruby$RUBY_VERSION \  
ruby$RUBY_VERSION-dev \  
libicu-dev git libkrb5-dev cmake build-essential \  
imagemagick libmagickwand-dev phantomjs wkhtmltopdf file sphinxsearch xvfb
curl &&\  
localedef ru_RU.UTF-8 -i ru_RU -fUTF-8 &&\  
locale-gen ru_RU.UTF-8 &&\  
# install NODE  
curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
&& \  
# clean up  
rm -rf /var/lib/apt/lists/* && \  
truncate -s 0 /var/log/*log && \  
# Setup Rubygems  
echo 'gem: --no-document' > /etc/gemrc && \  
gem install bundler && gem install static_code_analyzer -v "=0.1.2" && gem
update --system && \  
# Setup node packages  
npm install -g jshint  

