# Credit to https://github.com/cnry/dockerfiles  
#  
FROM debian:jessie  
MAINTAINER ccg <ccgdevops@googlegroups.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install Ruby  
RUN apt-get update && apt-get install -yqq \  
ruby \  
rubygems-integration \  
git \  
&& apt-get clean  
  
# install fake-s3 with bison's fix for
https://github.com/jubos/fake-s3/issues/66  
RUN gem install fakes3 -v 0.1.6.1  
ENV FAKES3_VERSION 0.1.6.1  
ENV FAKES3_BRANCH missing-content-type  
ENV FAKES3_REPO https://github.com/bison/fake-s3.git  
  
RUN git clone \--branch $FAKES3_BRANCH $FAKES3_REPO /tmp/fake-s3 \  
&& cd /tmp/fake-s3 \  
&& gem build fakes3.gemspec \  
&& gem install ./fakes3-$FAKES3_VERSION.gem  
  
# run fake-s3  
RUN mkdir -p /data/fakes3  
  
EXPOSE 4569  
ENTRYPOINT ["/usr/local/bin/fakes3"]  
# CMD ["-r", "/data", "-p", "4569", "-h", "0.0.0.0"]  
CMD ["-r", "/data", "-p", "4569"]  

