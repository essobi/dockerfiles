FROM buildpack-deps:jessie  
  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
# some of ruby's build scripts are written in ruby  
# we purge system ruby later to make sure our final image uses what we just
built  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
wget \  
curl \  
git \  
zlib1g-dev \  
libssl-dev \  
libreadline-dev \  
libyaml-dev \  
libxml2-dev \  
libxslt-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CFLAGS '-O2 -fno-tree-dce -fno-optimize-sibling-calls'  
RUN cd /usr/src && \  
wget https://storage.googleapis.com/google-code-archive-
downloads/v2/code.google.com/rubyenterpriseedition/ruby-
enterprise-1.8.7-2012.02.tar.gz && \  
tar xzf ruby-enterprise-1.8.7-2012.02.tar.gz && \  
cd /usr/src/ruby-enterprise-1.8.7-2012.02/ && \  
./installer --auto /usr/local \--dont-install-useful-gems --no-tcmalloc --no-
dev-docs  
  
ENV BUNDLER_VERSION 1.3.5  
RUN gem install bundler --version "$BUNDLER_VERSION"  
  
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
  
CMD [ "irb" ]  

