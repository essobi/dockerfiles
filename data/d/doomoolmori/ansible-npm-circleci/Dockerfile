FROM ubuntu:artful-20180417  
  
ENV DOCKER_PKG_VERSION="18.03.1~ce-0~ubuntu"  
  
RUN apt-get -y update \  
&& apt-get install -y --no-install-recommends ansible rsync ssh curl make git
apt-utils \  
&& rm -rf /var/lib/apt/lists/*  
# install node 8 and yarn  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install -y \  
nodejs \  
yarn \  
libpng-dev \  
zlib1g-dev \  
build-essential \  
pkg-config \  
&& rm -rf /var/lib/apt/lists/*  
# Install docker  
RUN apt-get install -y --no-install-recommends apt-transport-https ca-
certificates curl \  
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \  
&& echo \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable" | tee /etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& apt-get install -y docker-ce=$DOCKER_PKG_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD test.sh /tmp/test.sh  

