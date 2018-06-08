FROM alpine:3.5  
MAINTAINER make.io <info@make.io>  
  
ENV AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXXXXXXX  
ENV AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  
ENV AWS_REGION=ap-northeast-1  
ENV BUNDLER_VERSION=1.14.5  
ENV K8S_VERSION=1.5.3  
RUN apk add --update-cache \  
bash \  
openssh \  
curl \  
build-base \  
ruby \  
ruby-io-console \  
ruby-dev && \  
rm -rf /var/cache/apk/*  
  
# add kubectl for being able to smoketest kubernetes clusters with serverspec  
RUN curl -L https://storage.googleapis.com/kubernetes-
release/release/v"${K8S_VERSION}"/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl  
  
# skip installing gem documentation  
RUN echo 'gem: --no-rdoc --no-ri' >> /etc/gemrc  
  
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
  
COPY Gemfile /tmp  
COPY Gemfile.lock /tmp  
  
WORKDIR /tmp  
RUN bundle install  
  
RUN mkdir /projectfiles  
WORKDIR /projectfiles  

