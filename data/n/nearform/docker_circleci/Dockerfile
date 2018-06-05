FROM circleci/node:8.11-stretch  
LABEL maintainer alex.knol@nearform.com  
  
ENV S2I_VERSION v1.1.9a  
ENV SKOPEO_VERSION 0.1.28  
  
RUN \  
cd ~ && \  
S2I_VERSION_COMPLETE="$S2I_VERSION-40ad911d" && \  
URL="https://github.com/openshift/source-to-
image/releases/download/$S2I_VERSION/source-to-image-$S2I_VERSION_COMPLETE-
linux-amd64.tar.gz" && \  
wget "$URL" && \  
tar zxvf "source-to-image-$S2I_VERSION_COMPLETE-linux-amd64.tar.gz" && \  
sudo mv ./s2i /usr/local/bin && \  
curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip awscli-bundle.zip && \  
sudo apt-get update -qq && \  
sudo apt-get install -qqy \  
python-dev \  
python-setuptools \  
build-essential \  
jq \  
golang \  
git-core \  
libdevmapper-dev \  
libgpgme11-dev \  
btrfs-tools \  
go-md2man \  
libglib2.0-dev \  
libostree-dev && \  
sudo rm -rf /var/lib/apt/lists/* && \  
sudo easy_install pip && \  
sudo pip install https://github.com/goldmann/docker-squash/archive/master.zip
&& \  
sudo pip install python-dateutil && \  
sudo pip install --no-deps s3cmd && \  
sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
mkdir -p ${HOME}/go/ && \  
export GOPATH=${HOME}/go/ && \  
git clone https://github.com/projectatomic/skopeo
$GOPATH/src/github.com/projectatomic/skopeo && \  
cd $GOPATH/src/github.com/projectatomic/skopeo && make binary-local && \  
sudo mv skopeo /usr/bin/  

