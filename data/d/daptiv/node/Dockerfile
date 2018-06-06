FROM node:6-slim  
  
# to install yarn from apt, we need to configure the repository for yarn  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https \  
bzip2 \  
g++ \  
git \  
make \  
python \  
supervisor \  
unzip \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install -y --no-install-recommends \  
yarn \  
&& apt-get remove -y apt-transport-https \  
&& rm /etc/apt/sources.list.d/yarn.list \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN export CONSUL_TEMPLATE_VERSION=0.16.0 \  
&& export TMP_BUILD_DIR="$(mktemp -d)" \  
&& cd $TMP_BUILD_DIR \  
&& curl -s -L -O https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS \  
&& sed -i '/linux_amd64/!d' consul-
template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS \  
&& curl -s -L -O "https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \  
&& sha256sum -c consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS \  
&& unzip -d /usr/bin consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& chmod a=rx /usr/bin/consul-template \  
&& cd \- \  
&& rm -r $TMP_BUILD_DIR  
  
RUN adduser --disabled-password --gecos '' docker_user \  
&& mkdir /src \  
&& chown docker_user:docker_user /src  
  
WORKDIR /src  

