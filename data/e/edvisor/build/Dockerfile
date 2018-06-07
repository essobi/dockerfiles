FROM edvisor/node:5  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY preferences /etc/apt/preferences  
  
RUN apt-get update \  
&& apt-get install --assume-yes --no-install-recommends \  
apt-transport-https \  
software-properties-common \  
&& curl --silent --show-error --location
https://download.docker.com/linux/debian/gpg | apt-key add \- \  
&& curl --silent --show-error --location https://packagecloud.io/github/git-
lfs/gpgkey | apt-key add \- \  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/debian jessie stable" \  
&& add-apt-repository "deb https://packagecloud.io/github/git-lfs/debian/
jessie main" \  
&& add-apt-repository "deb http://deb.debian.org/debian testing main" \  
&& apt-get update \  
&& apt-get install --assume-yes --no-install-recommends \  
docker-ce \  
git-lfs \  
&& apt-get install --assume-yes --no-install-recommends --target-release
testing \  
ruby \  
mariadb-client \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl --silent --show-error https://s3.amazonaws.com/aws-cli/awscli-
bundle.zip --output awscli-bundle.zip \  
&& unzip awscli-bundle.zip \  
&& ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \  
&& rm -rf awscli-bundle awscli-bundle.zip  
  
RUN gem install aws-sdk bundler unirest --no-document  

