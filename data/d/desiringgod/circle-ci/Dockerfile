FROM ruby:2.5.1  
RUN apt-get update -y  
  
RUN apt-get install -y \  
xvfb \  
zip \  
unzip \  
redis-tools \  
libnss3-tools  
  
# from https://github.com/circleci/circleci-
images/blob/master/shared/images/Dockerfile-browsers.template  
RUN curl --silent --show-error --location --fail --retry 3 --output
/tmp/google-chrome-stable_current_amd64.deb
https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \  
&& (dpkg -i /tmp/google-chrome-stable_current_amd64.deb || apt-get -fy
install) \  
&& rm -rf /tmp/google-chrome-stable_current_amd64.deb \  
&& sed -i 's|HERE/chrome"|HERE/chrome" --disable-setuid-sandbox --no-
sandbox|g' \  
"/opt/google/chrome/google-chrome" \  
&& google-chrome --version  
  
RUN export CHROMEDRIVER_RELEASE=$(curl --location --fail --retry 3
http://chromedriver.storage.googleapis.com/LATEST_RELEASE) \  
&& curl --silent --show-error --location --fail --retry 3 --output
/tmp/chromedriver_linux64.zip
"http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_RELEASE/chromedriver_linux64.zip"
\  
&& cd /tmp \  
&& unzip chromedriver_linux64.zip \  
&& rm -rf chromedriver_linux64.zip \  
&& mv chromedriver /usr/local/bin/chromedriver \  
&& chmod +x /usr/local/bin/chromedriver \  
&& chromedriver --version  
  
# from https://github.com/nodejs/docker-
node/blob/2924f142789842282890f7b1736578b49b3be78f/8.5/Dockerfile  
RUN groupadd --gid 1000 node \  
&& useradd --uid 1000 --gid node --shell /bin/bash --create-home node  
  
# gpg keys listed at https://github.com/nodejs/node#release-team  
RUN set -ex \  
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
; do \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 8.5.0  
RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \  
&& case "${dpkgArch##*-}" in \  
amd64) ARCH='x64';; \  
ppc64el) ARCH='ppc64le';; \  
s390x) ARCH='s390x';; \  
arm64) ARCH='arm64';; \  
armhf) ARCH='armv7l';; \  
*) echo "unsupported architecture"; exit 1 ;; \  
esac \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
ENV YARN_VERSION 1.0.1  
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
  
# from https://github.com/wernight/docker-phantomjs/blob/master/Dockerfile  
# Install runtime dependencies  
RUN apt-get install -y --no-install-recommends \  
ca-certificates \  
bzip2 \  
libfontconfig \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -x \  
# Install official PhantomJS release  
&& mkdir /tmp/phantomjs \  
&& curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
| tar -xj --strip-components=1 -C /tmp/phantomjs \  
&& mv /tmp/phantomjs/bin/phantomjs /usr/local/bin \  
# Install dumb-init (to handle PID 1 correctly).  
# https://github.com/Yelp/dumb-init  
&& curl -Lo /tmp/dumb-init.deb https://github.com/Yelp/dumb-
init/releases/download/v1.1.3/dumb-init_1.1.3_amd64.deb \  
&& dpkg -i /tmp/dumb-init.deb \  
# Clean up  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/* \  
\  
# Run as non-root user.  
&& useradd --system --uid 65001 -m --shell /usr/sbin/nologin phantomjs \  
&& su phantomjs -s /bin/sh -c "phantomjs --version"  
  
# from https://github.com/circleci/circleci-
images/blob/master/shared/images/Dockerfile-basic.template#L32-L67  
# Install Docker  
# Docker.com returns the URL of the latest binary when you hit a directory
listing  
# We curl this URL and `grep` the version out.  
# The output looks like this:  
#> # To install, run the following commands as root:  
#> curl -fsSLO
https://download.docker.com/linux/static/stable/x86_64/docker-17.05.0-ce.tgz
&& tar --strip-components=1 -xvzf docker-17.05.0-ce.tgz -C /usr/local/bin  
#>  
#> # Then start docker in daemon mode:  
#> /usr/local/bin/dockerd  
RUN set -ex \  
&& export DOCKER_VERSION=$(curl --silent --fail --retry 3
https://download.docker.com/linux/static/stable/x86_64/ | grep -o -e
'docker-[.0-9]*-ce\\.tgz' | sort -r | head -n 1) \  
&&
DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/${DOCKER_VERSION}"
\  
&& echo Docker URL: $DOCKER_URL \  
&& curl --silent --show-error --location --fail --retry 3 --output
/tmp/docker.tgz "${DOCKER_URL}" \  
&& ls -lha /tmp/docker.tgz \  
&& tar -xz -C /tmp -f /tmp/docker.tgz \  
&& mv /tmp/docker/* /usr/bin \  
&& rm -rf /tmp/docker /tmp/docker.tgz \  
&& which docker \  
&& (docker version || true)  
  
# docker compose  
RUN COMPOSE_URL="https://circle-downloads.s3.amazonaws.com/circleci-
images/cache/linux-amd64/docker-compose-latest" \  
&& curl --silent --show-error --location --fail --retry 3 --output
/usr/bin/docker-compose $COMPOSE_URL \  
&& chmod +x /usr/bin/docker-compose \  
&& docker-compose version  
  
# install dockerize  
RUN DOCKERIZE_URL="https://circle-downloads.s3.amazonaws.com/circleci-
images/cache/linux-amd64/dockerize-latest.tar.gz" \  
&& curl --silent --show-error --location --fail --retry 3 --output
/tmp/dockerize-linux-amd64.tar.gz $DOCKERIZE_URL \  
&& tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-amd64.tar.gz \  
&& rm -rf /tmp/dockerize-linux-amd64.tar.gz \  
&& dockerize --version  
  
# from https://github.com/circleci/circleci-
images/blob/master/shared/images/Dockerfile-browsers.template  
# start xvfb automatically to avoid needing to express in circle.yml  
ENV DISPLAY :99  
RUN printf '#!/bin/sh\nXvfb :99 -screen 0 1280x1024x24 &\nexec "$@"\n' >
/tmp/entrypoint \  
&& chmod +x /tmp/entrypoint \  
&& mv /tmp/entrypoint /docker-entrypoint.sh  
  
# ensure that the build agent doesn't override the entrypoint  
LABEL com.circleci.preserve-entrypoint=true  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/bin/sh"]  

