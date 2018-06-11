# Do not edit - this file is generated from source/ci/root-
filesystem/Dockerfile.erb  
FROM ubuntu:latest  
# ubuntu:latest is LTS  
MAINTAINER s@uhlig.it  
  
# Basics  
ENV RUBY_VERSION=2.5  
RUN apt-get update && apt-get -y install --no-install-recommends \  
curl \  
ditaa \  
git \  
gpp \  
graphicsmagick \  
lmodern \  
locales \  
openssl \  
python \  
python-pip \  
software-properties-common \  
wget \  
&& apt-add-repository ppa:brightbox/ruby-ng && \  
apt-get update && \  
apt-get -y install \  
ruby"$RUBY_VERSION" \  
ruby"$RUBY_VERSION"-dev \  
&& gem install bundler --no-rdoc \  
&& rm -rf /var/lib/apt/lists/*  
  
# Set locale to UTF-8  
# https://stackoverflow.com/a/28406007/3212907  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen &&
locale-gen  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# git  
RUN git config --global user.email "s+concourse@uhlig.it" \  
&& git config --global user.name "Concourse Pipeline"  
  
# pandoc  
ENV PANDOC_DEB=`mktemp`  
RUN wget
"https://github.com/jgm/pandoc/releases/download/2.2.1/pandoc-2.2.1-1-amd64.deb"
-qO "$PANDOC_DEB" && dpkg -i "$PANDOC_DEB"; rm "$PANDOC_DEB"  
  
# cf  
ENV CF_CLI_DEB=`mktemp`  
RUN wget
"https://packages.cloudfoundry.org/stable?release=debian64&version=6.36.2" -qO
"$CF_CLI_DEB" && dpkg -i "$CF_CLI_DEB"; rm "$CF_CLI_DEB"  
  
# bx  
# https://console.bluemix.net/docs/cli/reference/bluemix_cli/download_cli.html  
RUN curl -fsSL https://clis.ng.bluemix.net/install/linux | sh  

