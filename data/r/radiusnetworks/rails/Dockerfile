FROM ruby:2.4.4  
ENV BUNDLER_VERSION="1.16.1"  
# Install Gem depencencies:  
# postgres: libpq-dev  
# nokogiri: libxml2-dev libxslt1-dev  
RUN apt-get update -qq && \  
apt-get install -y \  
build-essential \  
libpq-dev \  
libxml2-dev \  
libxslt1-dev \  
postgresql-client \  
netcat \  
nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Skip installing gem documentation and install bundler  
RUN echo -e 'install: --no-document\nupdate: --no-document' >> "/etc/gemrc" &&
\  
gem install bundler --version "$BUNDLER_VERSION" && \  
gem install foreman  
  
# install things globally, for great justice  
# and don't create ".bundle" in all our apps  
ENV GEM_HOME="/usr/local/bundle"  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH=$BUNDLE_BIN:$PATH  
  
ENV APP_HOME /app  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
CMD ["/bin/bash"]  

