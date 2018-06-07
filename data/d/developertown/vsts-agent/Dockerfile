FROM ubuntu:16.04  
  
ENV \  
VSTS_VERSION="2.105.2" \  
AGENT_FLAVOR=Generic  
  
# install vsts pre-reqs and basic build environment items  
RUN \  
apt-get update \  
&& apt-get install -y software-properties-common python-software-properties \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" >
/etc/apt/sources.list.d/docker.list \  
&& add-apt-repository ppa:git-core/ppa \  
&& apt-get install -y curl apt-transport-https \  
&& curl -LOs
http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu52_52.1-8ubuntu0.2_amd64.deb
\  
&& dpkg -i libicu52_52.1-8ubuntu0.2_amd64.deb \  
&& rm -f libicu52_52.1-8ubuntu0.2_amd64.deb \  
&& apt-get update \  
&& apt-get install -y \  
ca-certificates \  
libunwind8 \  
libcurl3 \  
build-essential \  
git \  
docker-engine  
  
# clean up and install vsts agent  
RUN \  
apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& adduser \  
\--disabled-password \  
\--home /usr/local/vsts-agent \  
\--shell /bin/bash \  
\--gecos "VSTS Agent" \  
\--ingroup docker \  
vsts  
  
WORKDIR /usr/local/vsts-agent  
USER vsts  
  
RUN \  
curl -Ls https://github.com/Microsoft/vsts-
agent/releases/download/v${VSTS_VERSION}/vsts-agent-
ubuntu.14.04-x64-${VSTS_VERSION}.tar.gz \  
| tar xvzf - \  
&& mkdir /usr/local/vsts-agent/_work  
  
# Copy in and run custom start wrapper  
COPY start.sh ./  
CMD ["./start.sh"]  

