FROM ubuntu:latest  
MAINTAINER Anthony Powles  
  
CMD ["/bin/bash", "-l"]  
  
# Latest versions can be found here:  
# - NodeJS: https://nodejs.org/en/  
# - Clojure: http://clojure.org/community/downloads  
# - Ruby: https://www.ruby-lang.org/en/downloads/  
# - Golang: https://golang.org/dl://golang.org/dl/  
ENV LANG=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
RBENV_ROOT=/opt/rbenv \  
RUBY_VERSION=2.3.0 \  
GO_VERSION=1.6 \  
GLIDE_VERSION=0.10.2 \  
GOROOT=/opt/go \  
NODE_VERSION=4.3.2 \  
CLOJURE_VERSION=1.8.0  
ENV PATH=$RBENV_ROOT/bin:$RBENV_ROOT/shims:$GOROOT/bin:/opt/node/bin:$PATH  
  
RUN groupadd deeva \  
&& useradd -m -s /bin/bash -g deeva deeva  
  
RUN locale-gen en_US.UTF-8 \  
&& apt-get update -y \  
&& apt-get install -qy --no-install-recommends \  
ca-certificates \  
curl \  
git \  
unzip \  
software-properties-common \  
build-essential \  
\  
libmysqlclient-dev \  
libffi-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
\  
openjdk-7-jdk \  
scala \  
&& add-apt-repository -y ppa:ondrej/php \  
&& apt-get update -y \  
&& apt-get install -qy --no-install-recommends \  
php7.0-cli \  
php7.0-common \  
libapache2-mod-php7.0 \  
php7.0 \  
php7.0-mysql \  
php7.0-fpm \  
php7.0-curl \  
\  
\  
\  
&& git clone https://github.com/rbenv/rbenv.git ${RBENV_ROOT} \  
&& git clone https://github.com/rbenv/ruby-build.git
${RBENV_ROOT}/plugins/ruby-build \  
&& echo 'export RBENV_ROOT='$RBENV_ROOT >> /etc/profile.d/rbenv.sh \  
&& echo 'export PATH="$RBENV_ROOT/bin:$PATH"' >> /etc/profile.d/rbenv.sh \  
&& echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh \  
&& chmod +x /etc/profile.d/rbenv.sh \  
&& echo "install: --no-rdoc --no-ri\nupdate: --no-rdoc --no-ri" > /etc/gemrc \  
&& rbenv install ${RUBY_VERSION} \  
&& rbenv global ${RUBY_VERSION} \  
&& gem update --system \  
&& gem install bundler \  
&& rbenv rehash \  
\  
\  
\  
&& curl -s https://storage.googleapis.com/golang/go${GO_VERSION}.linux-
amd64.tar.gz | tar -C /opt -zx \  
&& mkdir /opt/glide \  
&& curl -sL
https://github.com/Masterminds/glide/releases/download/${GLIDE_VERSION}/glide-${GLIDE_VERSION}-linux-
amd64.tar.gz | tar -C /opt/glide -zx \  
&& ln -s /opt/glide/linux-amd64/glide /usr/local/bin/glide \  
\  
\  
\  
&& curl -s
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz
| tar -C /opt -xJ \  
&& ln -s /opt/node-v${NODE_VERSION}-linux-x64 /opt/node \  
\  
\  
\  
&& curl -s
http://repo1.maven.org/maven2/org/clojure/clojure/${CLOJURE_VERSION}/clojure-${CLOJURE_VERSION}.zip
-o /opt/clojure.zip \  
&& unzip -q -d /opt /opt/clojure.zip \  
&& chmod 775 /opt/clojure-${CLOJURE_VERSION} \  
&& ln -s /opt/clojure-${CLOJURE_VERSION} /opt/clojure \  
&& rm /opt/clojure.zip \  
\  
\  
\  
&& apt-get clean \  
&& apt-get autoremove -y \  
&& apt-get remove --purge -y curl wget unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
# We removed curl, wget, unzip to make life harder for ill-intentioned users  
# Setup language environments  
  
RUN gem install rspec \  
&& mkdir -p /home/deeva/code/ruby/lib \  
&& cd /home/deeva/code/ruby \  
&& rspec --init \  
&& chown -R deeva:deeva /home/deeva/code  
  
USER deeva  
ENV DEEVA_RUNNER_RUBY_HOME=/home/deeva/code/ruby  
  

