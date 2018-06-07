FROM elixir:1.6.5  
MAINTAINER Andrea Usuelli <andrea.usuelli@prima.it>  
  
RUN apt-get update && apt-get install -qqy unzip \  
libncurses5 \  
groff \  
less \  
awscli \  
curl \  
tar \  
gzip \  
vim \  
tzdata \  
python2.7 \  
python-pip && \  
pip install awscli && \  
echo "Etc/UTC" > /etc/timezone && \  
apt-get purge -y unzip \  
wget && \  
rm -r /var/lib/apt/lists/* && \  
aws configure set default.s3.signature_version s3v4 && \  
aws configure set default.region eu-west-1 && \  
cd /opt && \  
curl -sLO https://github.com/dcoker/biscuit/releases/download/v0.1.3/biscuit-
linux_amd64.tgz && \  
tar xzvf biscuit-linux_amd64.tgz && \  
mv biscuit /usr/bin/biscuit && \  
chmod +x /usr/bin/biscuit && \  
rm biscuit-linux_amd64.tgz  
  
# TZ: https://github.com/primait/board/issues/1631  
# ENV TZ=:/etc/localtime  
  
ENV REPLACE_OS_VARS=true  
  
COPY files/setup_common.sh /setup_common.sh  
COPY files/decrypt_secrets.sh /decrypt_secrets.sh  
  
ENTRYPOINT ["/bin/bash"]  

