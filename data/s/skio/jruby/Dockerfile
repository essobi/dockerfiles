FROM ubuntu:xenial  
  
MAINTAINER Cameron Mullen <cam@skio.io>  
  
# Install base utilities  
RUN \  
apt-get update && \  
apt-get upgrade && \  
apt-get install -y \  
openjdk-8-jdk-headless \  
wget && \  
apt-get clean  
  
# Installing JRUBY  
ENV JRUBY_VERSION=9.1.0.0  
RUN \  
wget https://s3.amazonaws.com/jruby.org/downloads/$JRUBY_VERSION/jruby-
bin-$JRUBY_VERSION.tar.gz && \  
tar -xf jruby-bin-$JRUBY_VERSION.tar.gz && \  
rm jruby-bin-$JRUBY_VERSION.tar.gz && \  
mv jruby-$JRUBY_VERSION /jruby && \  
ln -s /jruby/bin/jruby /jruby/bin/ruby && \  
/jruby/bin/jruby -S gem install bundler --no-document  
  
ENV PATH=$PATH:/jruby/bin  

