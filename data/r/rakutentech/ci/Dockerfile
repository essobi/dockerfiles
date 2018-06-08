FROM debian:jessie  
  
RUN apt-get update -y && \  
apt-get install --no-install-recommends -y -q \  
procps \  
curl \  
wget \  
zip \  
build-essential \  
libssl-dev \  
libreadline-dev \  
zlib1g-dev \  
ca-certificates \  
git \  
mercurial \  
bzr && \  
apt-get --no-install-recommends dist-upgrade -y && \  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/*  
  
ENV RUBY_VERSION 2.4.2  
RUN git clone \--depth 1 https://github.com/rbenv/rbenv.git ~/.rbenv && \  
git clone \--depth 1 https://github.com/rbenv/ruby-build.git
~/.rbenv/plugins/ruby-build && \  
echo 'eval "$(~/.rbenv/bin/rbenv init -)"' >> ~/.bashrc && \  
~/.rbenv/bin/rbenv install ${RUBY_VERSION} && \  
~/.rbenv/bin/rbenv global ${RUBY_VERSION}  
  
ENV GO_VERSION 1.9  
ENV GOPATH /gopath  
ENV GOROOT /goroot  
RUN mkdir -p $GOROOT && mkdir -p $GOPATH  
RUN curl https://storage.googleapis.com/golang/go${GO_VERSION}.linux-
amd64.tar.gz | tar xvzf - -C $GOROOT \--strip-components=1  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
ENV JQ_VERSION 1.5  
RUN curl -L -S
"https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64"
>/usr/local/bin/jq && \  
chmod a+x /usr/local/bin/jq  
  
ENV SPIFF_VERSION 1.0.8  
RUN curl -L -S "https://github.com/cloudfoundry-
incubator/spiff/releases/download/v${SPIFF_VERSION}/spiff_linux_amd64"
>/usr/local/bin/spiff && \  
chmod a+x /usr/local/bin/spiff  
  
ENV SPRUCE_VERSION 1.12.1  
RUN curl -L -S
"https://github.com/geofffranks/spruce/releases/download/v${SPRUCE_VERSION}/spruce-
linux-amd64" >/usr/local/bin/spruce && \  
chmod a+x /usr/local/bin/spruce  
  
ENV CF_VERSION 6.32.0  
RUN curl -L -S
"https://cli.run.pivotal.io/stable?release=linux64-binary&version=${CF_VERSION}"
| tar -xzC /usr/local/bin cf  
  
ENV BOSHCLI_VERSION 1.3262.26.0  
ENV BUNDLER_VERSION 1.15.4  
RUN eval "$(~/.rbenv/bin/rbenv init -)" && \  
gem install bosh_cli:${BOSHCLI_VERSION} bundler:${BUNDLER_VERSION} \--no-ri
--no-rdoc  
  
RUN curl -L https://raw.githubusercontent.com/hipchat/hipchat-
cli/master/hipchat_room_message > /usr/local/bin/hipchat_room_message && \  
chmod a+x /usr/local/bin/hipchat_room_message  

