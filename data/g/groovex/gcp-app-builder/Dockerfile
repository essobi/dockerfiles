FROM google/cloud-sdk:latest  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y \--no-install-recommends \  
openssh-client nodejs yarn mercurial make fakeroot jq ruby ruby-dev cmake g++
pkg-config && \  
rm -rf /var/lib/apt/lists/*  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
421C365BD9FF1F717815A3895523BAEEB01FA116  
  
# setup golang  
RUN curl -sL "https://storage.googleapis.com/golang/$(curl -s
https://golang.org/VERSION?m=text).linux-amd64.tar.gz" | tar xz -C /usr/local
&& ln -sf /usr/local/go/bin/go /usr/local/bin/go  
  
COPY copy/go-bin-deb /usr/local/bin  
  
# setup package_cloud  
RUN gem install package_cloud --no-ri \--no-rdoc  

