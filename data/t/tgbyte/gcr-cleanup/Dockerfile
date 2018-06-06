FROM tgbyte/cron  
  
MAINTAINER Thilo-Alexander Ginkel <tg@tgbyte.de>  
  
RUN set -x \  
&& apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
-q \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
lsb-release \  
&& sed -i "s/httpredir.debian.org/`curl -s -D -
http://httpredir.debian.org/demo/debian/ | awk '/^Link:/ { print $2 }' | sed
-e 's@<http://\\(.*\\)/debian/>;@\1@g'`/" /etc/apt/sources.list \  
&& export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" \  
&& (echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" >
/etc/apt/sources.list.d/google-cloud-sdk.list) \  
&& (curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add
-) \  
&& apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q \  
google-cloud-sdk \  
jq \  
&& adduser --uid 500 \--disabled-login --gecos "gcr.io Cleanup" \--no-create-
home --home /gcr-cleanup gcr-cleanup \  
&& mkdir /gcr-cleanup \  
&& chown gcr-cleanup:gcr-cleanup /gcr-cleanup \  
&& apt-get clean autoclean \  
&& apt-get -q autoremove --yes \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD bin/gcr-cleanup.sh /usr/local/bin  
ADD entrypoint.d/ /entrypoint.d/  

