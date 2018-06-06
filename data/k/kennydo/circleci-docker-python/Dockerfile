FROM ubuntu:14.04.5  
  
MAINTAINER chinesedewey@gmail.com  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
ENV DOCKERIZE_VERSION v0.4.0  
  
ENV PATH "${PATH}:/opt/cli_venv/bin"  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:maxmind/ppa \  
&& add-apt-repository -y ppa:deadsnakes/ppa \  
&& apt-get install -y wget \  
&& wget -qO - http://packages.confluent.io/deb/3.2/archive.key | sudo apt-key
add - \  
&& add-apt-repository -y "deb [arch=amd64]
http://packages.confluent.io/deb/3.2 stable main" \  
&& apt-get update \  
&& apt-get install -y \  
curl \  
git-all \  
language-pack-id \  
libcurl4-openssl-dev \  
libffi-dev \  
libjpeg-dev \  
libmaxminddb-dev \  
libmaxminddb0 \  
libmysqlclient-dev \  
libpng-dev \  
libpq-dev \  
librdkafka++1 \  
librdkafka-dev \  
librdkafka-dev \  
librdkafka1 \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
mmdb-bin \  
mysql-client \  
ntp \  
postgresql-client \  
python3.6 \  
python3.6-dev \  
python3.6-venv \  
unzip \  
zlib1g-dev \  
&& apt-get clean  
  
RUN mkdir /usr/share/GeoIP && \  
chmod 755 /usr/share/GeoIP && \  
cd /usr/share/GeoIP/ && \  
wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
&& \  
tar xzvf GeoLite2-City.tar.gz && \  
mv GeoLite2-City_*/GeoLite2-City.mmdb GeoIP2-City.mmdb && \  
rm -r GeoLite2-City_* GeoLite2-City.tar.gz && \  
chmod 444 GeoIP2-City.mmdb  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O
/usr/local/bin/jq \  
&& chmod a+x /usr/local/bin/jq  
  
RUN python3.6 -m venv /opt/cli_venv \  
&& /opt/cli_venv/bin/pip install --upgrade awscli requests \  
&& rm -r /root/.cache/pip  

