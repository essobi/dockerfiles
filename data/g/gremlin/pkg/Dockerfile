FROM ubuntu:16.04  
RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y \  
aptly \  
cmake \  
cron \  
curl \  
file \  
git \  
g++ \  
python \  
make \  
man \  
nano \  
ruby \  
ruby-dev \  
rubygems \  
sudo \  
screen \  
dnsutils \  
iputils-ping \  
net-tools \  
vim \  
ca-certificates \  
xz-utils \  
pkg-config \  
apt-file \  
xutils-dev \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
RUN gem install --no-ri --no-rdoc fpm  
RUN gem install pleaserun  
  
# Install the AWS CLI  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip"  
RUN unzip awscli-bundle.zip  
RUN sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
# Setup strong gpg preferences  
RUN mkdir /root/.gnupg  
RUN echo "personal-digest-preferences SHA512" > /root/.gnupg/gpg.conf  
RUN echo "cert-digest-algo SHA512" >> /root/.gnupg/gpg.conf  
RUN echo "default-preference-list SHA512 SHA384 SHA256 SHA224 AES256 AES192
AES CAST5 ZLIB BZIP2 ZIP Uncompressed" >> /root/.gnupg/gpg.conf

