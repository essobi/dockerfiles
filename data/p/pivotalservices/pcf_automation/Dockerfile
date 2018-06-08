FROM ubuntu:latest  
  
MAINTAINER Caleb Washburn "cwashburn@pivotal.io"  
  
COPY stemcell-downloader-linux /usr/bin/stemcell-downloader-linux  
COPY cf /usr/bin/cf  
COPY autopilot-linux .  
ADD https://github.com/pivotal-cf/om/releases/download/0.23.0/om-linux
/usr/bin/om-linux  
ADD https://dl.minio.io/client/mc/release/linux-amd64/mc /usr/bin/mc  
RUN chmod +x /usr/bin/mc && chmod +x /usr/bin/cf && cf --version && chmod +x
autopilot-linux && cf install-plugin autopilot-linux -f && \  
chmod +x /usr/bin/om-linux && om-linux --version && \  
chmod +x /usr/bin/stemcell-downloader-linux && \  
apt-get update -y && apt-get install -yq build-essential \  
ruby ruby-dev \  
libxml2-dev \  
libxml2-utils \  
libsqlite3-dev \  
libxslt1-dev \  
libpq-dev \  
libmysqlclient-dev \  
prips \  
wget \  
gcc \  
gcc-multilib \  
git \  
uuid \  
uuid-dev \  
perl \  
curl \  
jq \  
unzip \  
libssl-dev \  
perl-doc \  
liburi-perl \  
libxml-libxml-perl \  
libcrypt-ssleay-perl \  
python-pip \  
python-dev \  
zlib1g-dev \  
vim-tiny \  
git && \  
apt-get clean && gem install cf-uaac --no-ri --no-rdoc && \  
gem install bosh_cli --no-ri --no-rdoc  

