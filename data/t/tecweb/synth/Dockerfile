FROM java:8-jdk  
  
RUN apt-get update && apt-get install -y libc6-dev --no-install-recommends &&
rm -rf /var/lib/apt/lists/*  
  
ENV JRUBY_VERSION 1.6.8  
ENV JRUBY_SHA1 0c321d2192768dfec419bee6b44c7190f4db32e1  
RUN mkdir /opt/jruby \  
&& curl -fSL
https://s3.amazonaws.com/jruby.org/downloads/${JRUBY_VERSION}/jruby-
bin-${JRUBY_VERSION}.tar.gz -o /tmp/jruby.tar.gz \  
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
  
RUN mkdir /var/synth  
  
ADD . /var/synth  
  
WORKDIR /var/synth  
  
VOLUME /var/synth/applications  
  
RUN jgem install bundler  
  
RUN bundle install  
  
EXPOSE 3000  
CMD [ "jruby", "--1.9", "-S", "script/server", "-b", "0.0.0.0" ]

