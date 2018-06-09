FROM ruby:2.3.1  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
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
  
# CUSTOMIZED --------------------------------------------------  
RUN mkdir /app  
WORKDIR /app  
ADD app/Gemfile /app/Gemfile  
ADD app/Gemfile.lock /app/Gemfile.lock  
RUN bundle install  
ADD ./app /app  
  
ENV PORT 5678  
EXPOSE 80 $PORT  
#EXPOSE 80  
CMD ["foreman", "start", "-d", "/app"]  
  

