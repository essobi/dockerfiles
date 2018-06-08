# YouEarnedIt Ops ops@youearnedit.com  
# PassengerRails 2.3 Dockerfile  
FROM youearnedit/base:latest  
  
# Set important vars  
ENV APP_HOME /usr/src/app/  
ENV RUBY_VERSION 2.3  
ENV BUNDLER_VERSION 1.15  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 7.6.0  
ENV NPM_VERSION 4.3.0  
ENV YARN_VERSION 0.24.6  
# We'll have to do most of the install with root  
USER root  
  
# Create the app directory with perms  
RUN mkdir -p ${APP_HOME}  
RUN chown docker:docker ${APP_HOME}  
WORKDIR ${APP_HOME}  
  
## ---- Ruby, Gem and Bundler Install ----  
# Install ruby, and rails deps  
RUN apt-add-repository -y ppa:brightbox/ruby-ng \  
&& apt-get update \  
&& apt-get install -y \  
ruby${RUBY_VERSION} \  
ruby${RUBY_VERSION}-dev \  
# Rails timezone sources  
tzdata \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install and setup bundler  
RUN gem install -i /var/lib/gems/${RUBY_VERSION}.0 bundler -v
${BUNDLER_VERSION}  
ENV BUNDLE_APP_CONFIG /home/docker/.bundle  
  
# Setup the gem env as the docker user  
USER docker  
RUN echo "gem: --no-document" >> /home/docker/.gemrc \  
&& mkdir -p /home/docker/.gem/ruby/${RUBY_VERSION}.0/build_info \  
/home/docker/.gem/ruby/${RUBY_VERSION}.0/cache \  
/home/docker/.gem/ruby/${RUBY_VERSION}.0/doc \  
/home/docker/.gem/ruby/${RUBY_VERSION}.0/extensions \  
/home/docker/.gem/ruby/${RUBY_VERSION}.0/gems \  
/home/docker/.gem/ruby/${RUBY_VERSION}.0/specifications  
ENV GEM_HOME /home/docker/.gem/ruby/${RUBY_MAJOR}.0  
ENV PATH ${GEM_HOME}/bin:${PATH}  
USER root  
  
## ---- Node Install ----  
# Add Node GPG keys  
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
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "${key}"; \  
done  
  
# Download, verify and install node  
RUN curl -SLO
"https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz"
\  
&& curl -SLO "https://nodejs.org/dist/v${NODE_VERSION}/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep "node-v${NODE_VERSION}-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v${NODE_VERSION}-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v${NODE_VERSION}-linux-x64.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs \  
&& npm install -g npm@"${NPM_VERSION}" \  
&& npm cache clear  
  
## ---- Yarn Install ----  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install -y yarn=${YARN_VERSION}\\* \  
&& rm -rf /var/lib/apt/lists/*  
  
## ---- Passenger Install ----  
# Install Passenger with Nginx  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
561F9B9CAC40B2F7 \  
&& echo "deb https://oss-binaries.phusionpassenger.com/apt/passenger xenial
main" > /etc/apt/sources.list.d/passenger.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends nginx-extras passenger \  
&& rm -rf /var/lib/apt/lists/*  
  
# Let the docker user run nginx with ENV VARs  
RUN echo "docker ALL=(ALL) NOPASSWD: SETENV: /usr/sbin/nginx" >> /etc/sudoers  
  
# Setup Passenger native support as the docker user  
USER docker  
RUN passenger-config build-native-support  
USER root  
  
# Setup Nginx configuration  
RUN mkdir -p /usr/src/nginx/conf.d \  
/usr/src/nginx/location.d \  
/usr/src/nginx/main.d  
COPY nginx.conf.erb /usr/src/nginx/nginx.conf.erb  
COPY main.d/* /usr/src/nginx/main.d/  
  
# Ensure Nginx config dir owned by the docker user  
RUN chown docker:docker -R /usr/src/nginx  
  
# Link stderr / stdout to nginx error / access logs  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
## ---- Setup final things and run ----  
# Setup entrypoint script  
COPY entrypoint.sh /usr/src/entrypoint.sh  
CMD ["/usr/src/entrypoint.sh"]  
  
# Become the docker user and GO!  
USER docker  
EXPOSE 80

