FROM phusion/baseimage:0.10.1  
LABEL CloudFactory <devops@cloudfactory.com>  
  
ENV RUBY_VERSION 2.4.4  
ENV BUNDLER_VERSION 1.16.1  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"
&& \  
apt-get install -y curl ca-certificates git build-essential libtool autoconf
deborphan && \  
apt-get -y clean && apt-get -y autoclean && apt-get -y autoremove && \  
deborphan | xargs apt-get remove --purge -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -SL https://github.com/postmodern/chruby/archive/v0.3.9.tar.gz | tar
-xzvC /tmp && \  
cd /tmp/chruby-0.3.9 && make install && \  
cd .. && rm -rf chruby-0.3.9  
  
RUN curl -SL https://github.com/postmodern/ruby-install/archive/master.tar.gz
| tar -xzvC /tmp && \  
cd /tmp/ruby-install-master && make install && \  
cd .. && rm -rf ruby-install-master  
  
RUN apt-get update && apt-get install -y ruby && \  
ruby-install \  
-p https://raw.github.com/skaes/rvm-patchsets/master/patches/ruby/${RUBY_VERSION}/railsexpress/01-skip-broken-tests.patch \  
-p https://raw.github.com/skaes/rvm-patchsets/master/patches/ruby/${RUBY_VERSION}/railsexpress/02-improve-gc-stats.patch \  
-p https://raw.github.com/skaes/rvm-patchsets/master/patches/ruby/${RUBY_VERSION}/railsexpress/03-display-more-detailed-stack-trace.patch \  
ruby ${RUBY_VERSION} \-- --disable-install-rdoc --enable-shared CFLAGS="-O3"
&& \  
rm -rf /usr/local/src && \  
apt-get remove --purge -y ruby && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo '[ -n "$BASH_VERSION" ] || [ -n "$ZSH_VERSION" ] || return' >>
/etc/profile.d/chruby.sh && \  
echo 'source /usr/local/share/chruby/chruby.sh' >> /etc/profile.d/chruby.sh &&
\  
echo 'chruby ruby' >> /etc/profile.d/default_ruby.sh && \  
chruby-exec ruby -- gem install bundler --version "$BUNDLER_VERSION"  
  
# install things sort of globally so that we could use shared space  
# as poor man's way of gem caching maybe  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH /opt/rubies/ruby-${RUBY_VERSION}/bin:$BUNDLE_BIN:$PATH  
  
  
#Making bundle fast  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN"&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"
&& \  
{ \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} > ~/.gemrc && \  
{ \  
echo '---'; \  
echo 'BUNDLE_JOBS: '3''; \  
} > $BUNDLE_APP_CONFIG/config  

