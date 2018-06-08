FROM ubuntu:16.04  
RUN cat /etc/apt/sources.list | sed -e 's|http://[^
]*|mirror://mirrors.ubuntu.com/mirrors.txt|g' > /tmp/sources.list && mv
/tmp/sources.list /etc/apt/sources.list  
RUN apt-get update && \  
apt-get install -y software-properties-common git-core build-essential
autoconf ruby ruby2.2 ruby2.2-dev && \  
gem install bundler omnibus berkshelf test-kitchen --no-doc  

