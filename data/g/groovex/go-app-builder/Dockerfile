FROM ubuntu:16.04  
  
RUN apt-get update -qq && apt-get install -y \--no-install-recommends curl ca-
certificates apt-transport-https software-properties-common && \  
add-apt-repository ppa:maarten-fonville/protobuf && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
\  
apt-get install -y \--no-install-recommends \  
openssh-client net-tools iputils-ping \  
nodejs yarn git mercurial fakeroot jq ruby ruby-dev cmake pkg-config build-
essential gdb \  
protobuf-compiler \  
redis-server libzmq3-dev chromium-browser && \  
rm -rf /var/lib/apt/lists/*  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
421C365BD9FF1F717815A3895523BAEEB01FA116  
  
# setup golang  
RUN curl -sL "https://storage.googleapis.com/golang/$(curl -s
https://golang.org/VERSION?m=text).linux-amd64.tar.gz" | tar xz -C /usr/local
&& ln -sf /usr/local/go/bin/go /usr/local/bin/go  
  
# setup go-bin-deb  
RUN VERSION=$(curl -s https://api.github.com/repos/groove-x/go-bin-
deb/releases/latest | jq '.tag_name' -r) && curl -sLO
https://github.com/groove-x/go-bin-deb/releases/download/$VERSION/go-bin-deb-
amd64.deb && dpkg -i go-bin-deb-amd64.deb && rm go-bin-deb-amd64.deb  
  
# setup package_cloud  
RUN gem install rake && gem install package_cloud --no-ri \--no-rdoc  
  
# setup gcloud  
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \-
&& \  
apt-get update && apt-get install -y google-cloud-sdk google-cloud-sdk-app-
engine-go && \  
rm -rf /var/lib/apt/lists/*  
  
# setup docker-ce  
RUN curl -sS https://download.docker.com/linux/ubuntu/gpg | apt-key add \- &&
\  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu
$(lsb_release -cs) stable" && \  
apt-get update && apt-get install -y docker-ce && \  
rm -rf /var/lib/apt/lists/*  

