FROM alpine:3.4  
MAINTAINER Make.io <info@make.io>  
  
ENV BUNDLER_VERSION=1.13.5  
# skip installing gem documentation  
RUN echo 'gem: --no-rdoc --no-ri' >> /etc/gemrc  
  
WORKDIR /tmp  
  
RUN apk add --update-cache \  
bash \  
groff \  
less \  
curl \  
jq \  
build-base \  
ruby-dev \  
ruby \  
ruby-io-console && \  
rm -rf /var/cache/apk/*  
  
RUN gem install bundler --version "$BUNDLER_VERSION"  
  
# install ruby gems globally, for great justice  
# and don't create ".bundle" in all our apps  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  
  
COPY Gemfile /tmp  
COPY Gemfile.lock /tmp  
  
RUN bundle install  
  
CMD ["bash"]

