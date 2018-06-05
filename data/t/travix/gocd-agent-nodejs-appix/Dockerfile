FROM travix/gocd-agent-gcloud:18.5.0  
  
MAINTAINER travix  
  
ENV JQ_VERSION="1.5+dfsg-1.3" \  
JQ_REPO="stretch" \  
NODEJS_VERSION="6"  
  
RUN (curl --silent \--location
"https://deb.nodesource.com/setup_${NODEJS_VERSION}.x" | bash -) \  
&& echo "deb http://httpredir.debian.org/debian stretch main" >>
/etc/apt/sources.list.d/stretch.list \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends -t $JQ_REPO jq=$JQ_VERSION \  
&& apt-get install -y \--no-install-recommends \  
aufs-tools \  
nodejs \  
&& curl -sSL https://raw.githubusercontent.com/Travix-
International/appix/master/appixinstall.sh | sh \  
&& cp /var/go/.appix/appix /usr/bin/appix \  
&& chmod a+x /var/go/.appix/appix \  
&& apt-get clean -y \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& npm install -g npm@^3.10.9 \  
&& npm install -g npm-cache@latest  

