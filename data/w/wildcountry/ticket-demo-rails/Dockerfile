FROM ruby:2.3.1-alpine  
MAINTAINER Rick Clare <rick@wildcountrytech.co.uk>  
LABEL Description="Ruby CI"  
ENTRYPOINT ["/bin/ash", "-c"]  
  
## Ruby prep  
RUN gem update --system  
RUN gem install bundler foreman  
  
## phantomjs 2.1.x (download binary)  
WORKDIR /tmp  
ENV PHANTOMJS_VERSION=2.1.1 PHANTOMJS_ARCH=linux-x86_64  
RUN wget -q -O /tmp/phantomjs-dockerized.tar.gz \  
"https://github.com/dustinblackman/phantomized/releases/download/${PHANTOMJS_VERSION}/dockerized-
phantomjs.tar.gz" \  
&& tar -xz -C / -f /tmp/phantomjs-dockerized.tar.gz  
RUN wget -q -O /tmp/phantomjs-${PHANTOMJS_VERSION}-${PHANTOMJS_ARCH}.tar.bz2 \  
"https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-${PHANTOMJS_ARCH}.tar.bz2"
\  
&& cd /tmp \  
&& tar xjf /tmp/phantomjs-${PHANTOMJS_VERSION}-${PHANTOMJS_ARCH}.tar.bz2 \  
&& cp /tmp/phantomjs-${PHANTOMJS_VERSION}-${PHANTOMJS_ARCH}/bin/phantomjs
/usr/local/bin/phantomjs \  
&& rm -rf /tmp/phantomjs-*  
  
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories  
  
# TODO: Replace postgresql-dev with libpq-dev package  
# if/when it becomes available for Alpine (i.e. libpq-dev is a small
dependency)  
RUN apk --no-cache add \  
build-base \  
git \  
libxml2-dev \  
libxslt-dev \  
# "postgresql-client@edge<9.6" \  
"postgresql-dev@edge<9.6" \  
"nodejs-lts@edge" \  
readline-dev \  
ruby-tzinfo  
  
## set timezone: https://wiki.alpinelinux.org/wiki/Setting_the_timezone  
RUN cp /usr/share/zoneinfo/Europe/London /etc/localtime \  
&& echo "Europe/London" > /etc/timezone  
  
WORKDIR /myapp  
  
RUN bundle config build.nokogiri --use-system-libraries && \  
bundle config without production:staging:demo && \  
bundle config jobs 3  
  
COPY .overcommit_gems.rb* /myapp/  
RUN bundle install --gemfile=.overcommit_gems.rb  
  
COPY Gemfile* /myapp/  
RUN bundle install  
  
# npm packages (via package.json)  
COPY package.json /myapp/  
RUN npm install --no-progress  
  
ENV PATH=./bin:./node_modules/.bin:/bundle/bin:$PATH \  
GIT_AUTHOR_NAME="Example name" \  
GIT_AUTHOR_EMAIL="example@example.com"  
COPY . /myapp  
  
## cleanup  
RUN rm -rf /tmp/* /var/tmp/*  

