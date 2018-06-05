FROM debian:jessie  
MAINTAINER Adam Bouqdib <adam@abemedia.co.uk>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
MYSQL_HOST=127.0.0.1 \  
MYSQL_PORT=3306 \  
MYSQL_USER=root \  
BATCH_SIZE=1000000  
  
RUN set -ex \  
&& apt-get update && apt-get install -yq --no-install-recommends \  
ca-certificates \  
curl \  
bash \  
apt-transport-https \  
&& echo "deb https://packages.cloud.google.com/apt cloud-sdk-jessie main" |
tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \  
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \-
\  
&& apt-get update && apt-get install -yq --no-install-recommends \  
mysql-client \  
google-cloud-sdk \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
ADD start.sh /start.sh  
  
CMD ["/start.sh"]  

