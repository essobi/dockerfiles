FROM ubuntu:xenial  
  
# install dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https \  
python3 \  
python3-dev \  
ipython3 \  
python3-setuptools \  
python3-software-properties \  
python3-scipy \  
python3-pil \  
python3-lxml \  
python3-crypto \  
python3-cryptography \  
python3-wheel \  
python3-ipdb \  
python3-psycopg2 \  
libpq-dev \  
libgeos-dev \  
gettext \  
git \  
pngquant \  
python3-pip \  
libatlas-base-dev \  
build-essential \  
ca-certificates \  
curl \  
wget  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
RUN pip3 install --upgrade newrelic safety boto3 docopt  
ADD safety.sh /usr/local/bin/safety.sh  
ADD get_secrets.py /usr/local/bin/get_secrets.py  

