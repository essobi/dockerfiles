FROM ubuntu:16.04  
# -- Dependencies --  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
git-core \  
libffi-dev \  
libgeos-dev \  
libpq-dev \  
libproj-dev \  
libreadline-dev \  
libssl-dev \  
tzdata \  
unzip  
  
## -- Ruby --  
ENV RUBY_VERSION=2.5.1  
RUN git clone https://github.com/rbenv/rbenv.git /root/.rbenv \  
&& git clone https://github.com/rbenv/ruby-build.git
/root/.rbenv/plugins/ruby-build  
ENV PATH /root/.rbenv/shims:/root/.rbenv/bin:$PATH  
RUN rbenv install $RUBY_VERSION \  
&& CONFIGURE_OPTS="--disable-install-doc" rbenv global $RUBY_VERSION \  
&& gem install bundler  
  
# -- Node --  
ENV NODE_VERSION=8.9.4  
RUN git clone https://github.com/nodenv/nodenv.git /root/.nodenv \  
&& git clone https://github.com/nodenv/node-build.git
/root/.nodenv/plugins/node-build \  
&& git clone https://github.com/nodenv/nodenv-package-rehash.git
/root/.nodenv/plugins/nodenv-package-rehash  
ENV PATH /root/.nodenv/shims:/root/.nodenv/bin:$PATH  
RUN nodenv install $NODE_VERSION \  
&& nodenv global $NODE_VERSION \  
&& nodenv rehash  
  
# -- Yarn --  
ENV YARN_VERSION=1.6.0  
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
  
# -- Google Chrome --  
RUN curl --silent --show-error --location --fail --retry 3 --output
/tmp/google-chrome-stable_current_amd64.deb
https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \  
&& (dpkg -i /tmp/google-chrome-stable_current_amd64.deb || apt-get -fy
install) \  
&& rm -rf /tmp/google-chrome-stable_current_amd64.deb \  
&& sed -i 's|HERE/chrome"|HERE/chrome" --disable-setuid-sandbox --no-
sandbox|g' "/opt/google/chrome/google-chrome" \  
&& google-chrome --version  
  
# -- ChromeDriver --  
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
  
CMD ["/bin/bash"]  

