FROM debian:jessie  
  
MAINTAINER Rodrigue Villetard  
# Copied from https://hub.docker.com/r/cnry/fake-s3/  
ENV DEBIAN_FRONTEND noninteractive  
ENV FAKE_S3_ROOT /srv/fake-s3  
  
RUN mkdir -p "$FAKE_S3_ROOT" && chown daemon:daemon "$FAKE_S3_ROOT"  
  
WORKDIR $FAKE_S3_ROOT  
  
RUN apt-get update \  
&& apt-get -y install ruby rubygems-integration git \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV FAKES3_VERSION 1.0.0  
ENV FAKES3_BRANCH master  
ENV FAKES3_REPO https://github.com/jchristi/fake-s3.git  
  
RUN git clone \--branch $FAKES3_BRANCH $FAKES3_REPO /tmp/fake-s3 \  
&& cd /tmp/fake-s3 \  
&& gem build fakes3.gemspec \  
&& gem install ./fakes3-$FAKES3_VERSION.gem  
  
ENV FAKE_S3_PORT 8080  
VOLUME ["/srv/fake-s3"]  
  
USER daemon  
  
CMD exec fakes3 server --port="$FAKE_S3_PORT" \--root="$FAKE_S3_ROOT"  
  

