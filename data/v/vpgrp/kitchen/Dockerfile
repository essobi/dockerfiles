# Copyright (c) 2017 Vente-Privée  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
  
FROM vpgrp/debian:stretch  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
TZ="Europe/Amsterdam"  
  
RUN curl --silent 'https://mirror.vpgrp.io/keys/docker.gpg' | \  
apt-key --keyring /etc/apt/trusted.gpg.d/docker-keyring.gpg add - && \  
echo 'deb https://mirror.vpgrp.io/debian-docker stretch stable' > \  
/etc/apt/sources.list.d/docker.list && \  
apt-get update -qq && \  
apt-get upgrade -qq -y && \  
apt-get install -qq -y \  
build-essential \  
dirmngr \  
docker-ce \  
lsb-release \  
puppet \  
ruby \  
ruby-dev \  
rubygems \  
sudo \  
systemd \  
systemd-sysv \  
wget \  
zlib1g-dev && \  
apt-clean  
  
# http://kitchen.ci/  
RUN gem install rake \  
\--no-document \  
\--quiet && \  
gem install bundler \  
\--no-document \  
\--quiet && \  
gem install kitchen-ansible \  
\--no-document \  
\--quiet && \  
gem install kitchen-docker \  
\--no-document \  
\--quiet && \  
gem install kitchen-docker_cli \  
\--no-document \  
\--quiet && \  
gem install kitchen-puppet \  
\--no-document \  
\--quiet && \  
gem install kitchen-verifier-serverspec \  
\--no-document \  
\--quiet && \  
gem install librarian-puppet \  
\--no-document \  
\--quiet && \  
gem install test-kitchen \  
\--no-document \  
\--quiet  
  
VOLUME [ "/sys/fs/cgroup", "/run", "/run/lock" ]  
  
CMD [ "/lib/systemd/systemd" ]  
# EOF  

