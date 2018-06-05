# ubuntu-openjdk-8-jdk  
#  
FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install the python script required for "add-apt-repository" and curl  
RUN apt-get update && apt-get install -y software-properties-common  
RUN add-apt-repository ppa:webupd8team/java  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
RUN apt-get update && apt-get install -y software-properties-common curl
oracle-java8-set-default  
  
# Sets language to UTF8 : this works in pretty much all cases  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
  
# Setup JAVA_HOME, this is useful for docker commandline  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/  
RUN export JAVA_HOME  
  
RUN apt-get install -y libc6-dev --no-install-recommends && rm -rf
/var/lib/apt/lists/*  
  
ENV JRUBY_VERSION 9.1.2.0  
ENV JRUBY_SHA256
60598a465883ab4c933f805de4a7f280052bddc793b95735465619c03ca43f35  
RUN mkdir /opt/jruby \  
&& curl -fSL
https://s3.amazonaws.com/jruby.org/downloads/${JRUBY_VERSION}/jruby-
bin-${JRUBY_VERSION}.tar.gz -o /tmp/jruby.tar.gz \  
&& echo "$JRUBY_SHA256 /tmp/jruby.tar.gz" | sha256sum -c - \  
&& tar -zx --strip-components=1 -f /tmp/jruby.tar.gz -C /opt/jruby \  
&& rm /tmp/jruby.tar.gz \  
&& update-alternatives --install /usr/local/bin/ruby ruby /opt/jruby/bin/jruby
1  
ENV PATH /opt/jruby/bin:$PATH  
  
# skip installing gem documentation  
RUN mkdir -p /opt/jruby/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /opt/jruby/etc/gemrc  
  
RUN gem install bundler  
  
# install things globally, for great justice  
# and don't create ".bundle" in all our apps  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  

