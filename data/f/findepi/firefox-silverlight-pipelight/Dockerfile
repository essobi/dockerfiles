FROM ubuntu:14.04  
MAINTAINER Piotr Findeisen <piotr.findeisen@gmail.com>  
  
RUN set -xe; \  
export DEBIAN_FRONTEND=noninteractive; \  
apt-get -y update; \  
apt-get install -y software-properties-common; `# add-apt-repository` \  
add-apt-repository -y ppa:pipelight/stable; `# pipelight` \  
apt-add-repository -y multiverse; `# ttf-mscorefonts-installer` \  
dpkg --add-architecture i386; `# wine-staging is i386` \  
apt-get -y update; \  
`# Allow installation of MS corefonts (pipelight dependency)` \  
echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula boolean
true | debconf-set-selections; \  
apt-get install -y --install-recommends \  
firefox \  
pipelight-multi; \  
pipelight-plugin --update; \  
pipelight-plugin --accept --enable silverlight; \  
rm -rf /var/lib/apt/lists/*; `# Purge apt-get cache` \  
echo "done"  
  
COPY setup-and-launch-firefox.sh /usr/local/bin/  

