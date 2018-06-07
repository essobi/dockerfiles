FROM alpine:3.4  
  
MAINTAINER Richard Jennings <richardjennings@gmail.com>  
  
ENV GITHUB_GEM_VERSION 111  
  
ENV BUILD_DEPS \  
gcc \  
g++ \  
make \  
curl \  
bison \  
ca-certificates \  
tzdata \  
ruby-dev \  
glib-dev \  
libc-dev \  
ruby-bundler \  
ruby-irb  
  
RUN apk --no-cache add $BUILD_DEPS ruby && \  
echo 'gem: --no-document' > /etc/gemrc && \  
gem install github-pages:${GITHUB_GEM_VERSION} && \  
apk del $BUILD_DEPS && \  
rm -rf /usr/lib/ruby/gems/2.3.0/cache && \  
mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
EXPOSE 4000  
  
CMD jekyll serve -d /_site --incremental -H 0.0.0.0 -P 4000  

