#FROM buildpack-deps:jessie  
#  
#RUN groupadd --gid 1000 node \  
# && useradd --uid 1000 --gid node --shell /bin/bash --create-home node  
#  
#  
#RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \  
# && case "${dpkgArch##*-}" in \  
# amd64) ARCH='x64';; \  
# ppc64el) ARCH='ppc64le';; \  
# s390x) ARCH='s390x';; \  
# arm64) ARCH='arm64';; \  
# armhf) ARCH='armv7l';; \  
# *) echo "unsupported architecture"; exit 1 ;; \  
# esac \  
# && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" \  
# && curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
# && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
# && grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt |
sha256sum -c - \  
# && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-
components=1 \  
# && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt \  
# && ln -s /usr/local/bin/node /usr/local/bin/nodejs  
#CMD [ "node" ]  
FROM ruby:2.4.0  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev
libmysqlclient-dev mysql-client expect  
  
# Install RMagick  
RUN apt-get install -y libmagickwand-dev imagemagick  
  
# Install Nokogiri  
RUN apt-get install -y zlib1g-dev  
  
# for capybara-webkit  
RUN apt-get install -y libqt4-webkit libqt4-dev xvfb  
  
# for node  
RUN apt-get install -y python python-dev python-pip python-virtualenv  
  
# install nodejs  
# gpg keys listed at https://github.com/nodejs/node#release-team  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 8.4.0  
RUN \  
cd /tmp && \  
wget http://nodejs.org/dist/node-latest.tar.gz && \  
tar xvzf node-latest.tar.gz && \  
rm -f node-latest.tar.gz && \  
cd node-v* && \  
./configure && \  
CXX="g++ -Wno-unused-local-typedefs" make && \  
CXX="g++ -Wno-unused-local-typedefs" make install && \  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
npm install -g npm && \  
echo '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  
  
ENV YARN_VERSION 0.27.5  
RUN set -ex \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  
  
RUN mkdir /app  
WORKDIR /app  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
RUN bundle install  
ADD . /app  
  
# (Optional) Set custom Unicorn configuration (if you have any)  
COPY config/unicorn/production.rb config/unicorn.rb  
# Set Nginx site configuration  
COPY config/nginx/development.conf /etc/nginx/sites-enabled/default  
  
# Automatically start the web server  
CMD gem install foreman && \  
RAILS_ENV=production bundle exec rake assets:precompile && \  
RAILS_ENV=production rake db:exists && rake db:migrate || rake db:setup && \  
foreman start -f Procfile  
  
#CMD ./bin/start.sh  
EXPOSE 3000

