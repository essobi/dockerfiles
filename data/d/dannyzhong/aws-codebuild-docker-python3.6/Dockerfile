# Copyright 2017-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.  
#  
# Licensed under the Amazon Software License (the "License"). You may not use
this file except in compliance with the License.  
# A copy of the License is located at  
#  
# http://aws.amazon.com/asl/  
#  
# or in the "license" file accompanying this file.  
#  
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, express or implied.  
# See the License for the specific language governing permissions and
limitations under the License.  
#  
# Ubuntu 17.10's python3 is 3.6.3 (as of 11/10/2017)  
# https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-
apt-get  
FROM ubuntu:17.10  
##########################################################################  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends dialog apt-utils #
https://github.com/moby/moby/issues/27988  
RUN apt-get install -y --no-install-recommends \  
python3 python3-pip python3-dev # python3-dev needed by awscli  
RUN apt-get install -y --no-install-recommends \  
wget fakeroot ca-certificates tar gzip zip \  
autoconf automake bzip2 file g++ gcc imagemagick libbz2-dev libc6-dev
libcurl4-openssl-dev \  
libdb-dev libevent-dev libffi-dev libgeoip-dev libglib2.0-dev libjpeg-dev
libkrb5-dev \  
liblzma-dev libmagickcore-dev libmagickwand-dev libmysqlclient-dev libncurses-
dev libpng-dev \  
libpq-dev libreadline-dev libsqlite3-dev libssl-dev libtool libwebp-dev
libxml2-dev libxslt-dev \  
libyaml-dev make patch xz-utils zlib1g-dev unzip curl git  
  
RUN apt-get install -y --no-install-recommends less  
RUN apt-get install -y --no-install-recommends vim  
  
RUN apt-get install --yes jq  
# upgrade jq to 1.5. http://stackoverflow.com/questions/36462955/upgrading-jq-
to-1-5-on-ubuntu  
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 \  
&& chmod +x jq-linux64 \  
&& mv jq-linux64 $(which jq)  
  
# Install node8. node7 can't be installed on ubuntu 17.10
(https://github.com/nodesource/distributions/issues/543)  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install --yes nodejs  
RUN pip3 install --upgrade pip setuptools  
RUN pip3 install --upgrade --user awscli  
  
RUN wget "https://bootstrap.pypa.io/get-pip.py" -O /tmp/get-pip.py \  
&& python3 /tmp/get-pip.py \  
&& pip3 install awscli==1.11.25 \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV DOCKER_BUCKET="get.docker.com" \  
DOCKER_VERSION="1.12.1" \  
DOCKER_SHA256="05ceec7fd937e1416e5dce12b0b6e1c655907d349d52574319a1e875077ccb79"
\  
DIND_COMMIT="3b5fac462d21ca164b3778647420016315289034"  
COPY dockerd-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/dockerd-entrypoint.sh #
https://github.com/moby/moby/issues/27182  
  
# From the docker:1.11  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v \  
# From the docker dind 1.11  
&& apt-get update && apt-get install -y --no-install-recommends \  
e2fsprogs iptables xfsprogs xz-utils \  
# set up subuid/subgid so that "--userns-remap=default" works out-of-the-box  
&& addgroup dockremap \  
&& useradd -g dockremap dockremap \  
&& echo 'dockremap:165536:65536' >> /etc/subuid \  
&& echo 'dockremap:165536:65536' >> /etc/subgid \  
&& wget
"https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind" -O
/usr/local/bin/dind \  
&& chmod +x /usr/local/bin/dind \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
VOLUME /var/lib/docker  
  
ENTRYPOINT ["dockerd-entrypoint.sh"]  
  

