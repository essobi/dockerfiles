FROM debian:wheezy  
MAINTAINER Jesse Reynolds @jessereynolds  
  
RUN apt-get update && apt-get install -y \  
git \  
curl \  
build-essential \  
ruby1.9.1-full \  
libssl-dev \  
libreadline-dev \  
libxslt1-dev \  
libxml2-dev \  
libcurl4-openssl-dev \  
zlib1g-dev \  
libexpat1-dev \  
libicu-dev \  
cmake  
  
RUN git config --global user.email "docker@flapjack.io" && \  
git config --global user.name "Flapjack Docker Packager"  
  
RUN gem install bundler --no-ri --no-rdoc  
  
RUN curl -o /tmp/go1.3.1.linux-amd64.tar.gz
https://storage.googleapis.com/golang/go1.3.1.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf /tmp/go1.3.1.linux-amd64.tar.gz && \  
echo "PATH=$PATH:/usr/local/go/bin" | tee /etc/profile.d/go.sh  
  
RUN git config --global user.email "docker@flapjack.io" && \  
git config --global user.name "Flapjack Docker Packager"  
  
RUN git clone https://github.com/flapjack/omnibus-flapjack.git && \  
cd omnibus-flapjack && \  
bundle install --binstubs  

