FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
#=============  
# Set WORKDIR  
#=============  
WORKDIR /root  
  
RUN apt-get -qqy update && \  
apt-get -qqy --no-install-recommends install \  
openjdk-8-jdk \  
ca-certificates \  
tzdata \  
zip \  
unzip \  
curl \  
wget \  
libqt5webkit5 \  
libgconf-2-4 \  
xvfb \  
&& rm -rf /var/lib/apt/lists/*  
  
#===============  
# Set JAVA_HOME  
#===============  
ENV JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre" \  
PATH=$PATH:$JAVA_HOME/bin  
  
#=====================  
# Install Android SDK  
#=====================  
ARG SDK_VERSION=sdk-tools-linux-3859397  
ARG ANDROID_BUILD_TOOLS_VERSION=26.0.0  
ARG ANDROID_PLATFORM_VERSION="android-25"  
ENV SDK_VERSION=$SDK_VERSION \  
ANDROID_BUILD_TOOLS_VERSION=$ANDROID_BUILD_TOOLS_VERSION \  
ANDROID_HOME=/root  
  
RUN wget -O tools.zip
https://dl.google.com/android/repository/${SDK_VERSION}.zip && \  
unzip tools.zip && rm tools.zip && \  
chmod a+x -R $ANDROID_HOME && \  
chown -R root:root $ANDROID_HOME  
  
ENV PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin  
  
# https://askubuntu.com/questions/885658/android-sdk-repositories-cfg-could-
not-be-loaded  
RUN mkdir -p ~/.android && \  
touch ~/.android/repositories.cfg && \  
echo y | sdkmanager "platform-tools" && \  
echo y | sdkmanager "build-tools;$ANDROID_BUILD_TOOLS_VERSION" && \  
echo y | sdkmanager "platforms;$ANDROID_PLATFORM_VERSION"  
  
ENV PATH=$PATH:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools  
  
  
  
#=====================  
# Install Ruby with dependencies  
#=====================  
RUN apt-get update  
RUN apt-get install -y build-essential  
RUN apt-get install -y libssl-dev  
RUN apt-get install -y git-core  
RUN apt-get install -y curl  
RUN apt-get clean  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
autoconf \  
automake \  
bzip2 \  
file \  
g++ \  
gcc \  
imagemagick \  
libbz2-dev \  
libc6-dev \  
libcurl4-openssl-dev \  
libdb-dev \  
libevent-dev \  
libffi-dev \  
libgeoip-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libkrb5-dev \  
liblzma-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpng-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libtool \  
libwebp-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
make \  
patch \  
xz-utils \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
RUN apt-get update && apt-get install -y curl procps && rm -rf
/var/lib/apt/lists/*  
  
ENV RUBY_MAJOR 2.1  
ENV RUBY_VERSION 2.1.5  
# some of ruby's build scripts are written in ruby  
# we purge this later to make sure our final image uses what we just built  
RUN apt-get update \  
&& apt-get install -y bison ruby \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/ruby \  
&& curl -SL "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.bz2" \  
| tar -xjC /usr/src/ruby --strip-components=1 \  
&& cd /usr/src/ruby \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& apt-get purge -y --auto-remove bison ruby \  
&& make install \  
&& rm -r /usr/src/ruby  
  
# skip installing gem documentation  
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"  
  
# install things globally, for great justice  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
RUN gem install bundler \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin"  
  
# don't create ".bundle" in all our apps  
ENV BUNDLE_APP_CONFIG $GEM_HOME

