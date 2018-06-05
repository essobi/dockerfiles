FROM ubuntu:trusty  
  
MAINTAINER Zac Bergquist "zbergquist@pivotal.io"  
MAINTAINER Josh Ghiloni "jghiloni@pivotal.io"  
  
#ENV bosh_artifact bosh-cli-2.0.28-linux-amd64  
ARG version  
  
RUN apt-get update -y && \  
apt-get install -y wget build-essential zlibc zlib1g-dev ruby ruby-dev openssl
libxslt-dev libxml2-dev libssl-dev libreadline6 libreadline6-dev libyaml-dev
libsqlite3-dev sqlite3 git && \  
wget https://s3.amazonaws.com/bosh-cli-artifacts/bosh-cli-${version}-linux-
amd64 && \  
install bosh-cli-${version}-linux-amd64 /usr/local/bin/bosh && \  
apt-get clean  

