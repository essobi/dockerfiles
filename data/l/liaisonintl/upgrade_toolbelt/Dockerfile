FROM alpine:3.4  
# These should be versioned  
RUN apk add --no-cache ruby=2.3.7-r0  
RUN apk add --no-cache ruby-dev=2.3.7-r0  
RUN apk add --no-cache ruby-irb=2.3.7-r0  
  
# These should remain unversioned  
RUN apk add --no-cache build-base  
RUN apk add --no-cache libffi-dev  
RUN apk add --no-cache ca-certificates # this should never be version pinned!  
RUN apk add --no-cache libxml2-dev  
RUN apk add --no-cache libxslt-dev  
  
RUN update-ca-certificates  
  
RUN echo 'gem: --no-rdoc --no-ri' >> /etc/gemrc  
  
RUN mkdir -p /opt/ci && \  
adduser -D -s /bin/bash ci && \  
chown ci: /opt/ci  
  
USER ci  
WORKDIR /opt/ci/  
  
ENV GEM_HOME=/home/ci/bundle  
ENV BUNDLE_PATH=${GEM_HOME}  
ENV BUNDLE_APP_CONFIG=${GEM_HOME}  
ENV BUNDLE_BIN=${GEM_HOME}/bin  
ENV PATH=${GEM_HOME}/bin:${PATH}  
  
RUN gem install bundler:1.16.1  
RUN gem install io-console:0.4.6  
  
COPY Gemfile Gemfile  
COPY Gemfile.lock Gemfile.lock  
RUN bundle install  
  
COPY . /opt/ci  
  
CMD /opt/ci/bin/travis_analyzer  

