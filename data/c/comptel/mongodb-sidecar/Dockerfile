FROM ubuntu:16.04  
# RUN apk update &&\  
# apk add --no-cache ca-certificates wget openssl\  
# make gcc ruby-dev build-base libc-dev linux-headers &&\  
# update-ca-certificates  
#  
#  
# RUN bundle config --global frozen 1  
ENV BUILD_PACKAGES="patch gcc make wget g++ \  
ruby2.3-dev libghc-zlib-dev"  
ENV PACKAGES="ruby2.3 ruby-switch bzip2 liblz4-tool ca-certificates git"  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-add-repository ppa:brightbox/ruby-ng && \  
apt-get update && \  
apt-get install -y $BUILD_PACKAGES && \  
apt-get install -y $PACKAGES && \  
ruby-switch --set ruby2.3 && \  
gem install bundler  
  
# WORKDIR /app  
RUN mkdir /cache  
COPY files/Gemfile /cache/Gemfile  
COPY files/Gemfile.lock /cache/Gemfile.lock  
RUN cd /cache && bundle install  
  
COPY files/ /app  
RUN cd /app && bundle install  
  
# RUN wget -O /app/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
# RUN chmod +x /app/dumb-init  
RUN chmod +x /app/sidecar.rb && \  
chmod +x /app/run.sh  
  
# RUN apt-get remove --purge -y $BUILD_PACKAGES && \  
# rm -rf /var/lib/apt/lists/* && \  
# apt-get clean && \  
# apt -y autoremove  
# ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
# CMD ["/app/init.rb"]  
ENTRYPOINT []  
CMD []  

