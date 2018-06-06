FROM instructure/ruby-passenger:2.1  
  
USER root  
RUN set -xe && \  
curl -sL https://deb.nodesource.com/setup_0.12 | bash - && \  
apt-get update -qq && \  
apt-get install -qq \  
nodejs \  
postgresql-client \  
libxmlsec1-dev \  
unzip \  
fontforge \  
\--no-install-recommends && \  
npm install -g gulp && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/* && \  
true  
# We will need sfnt2woff in order to build fonts  
WORKDIR /root  
RUN set -xe && \  
if [ -e /var/lib/gems/$RUBY_MAJOR.0/gems/bundler-* ]; then BUNDLER_INSTALL="-i
/var/lib/gems/$RUBY_MAJOR.0"; fi && \  
curl -O http://people.mozilla.org/~jkew/woff/woff-code-latest.zip && \  
unzip woff-code-latest.zip && \  
make && \  
cp sfnt2woff /usr/local/bin && \  
gem uninstall --all --ignore-dependencies --force $BUNDLER_INSTALL bundler &&
\  
gem install bundler --no-document -v 1.11.2 && \  
find $GEM_HOME ! -user docker | xargs chown docker:docker && \  
true  
  
USER docker  
WORKDIR /usr/src/app

