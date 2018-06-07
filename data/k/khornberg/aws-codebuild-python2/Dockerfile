# Copyright 2017-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.  
#  
# Licensed under the Amazon Software License (the "License"). You may not use
this file except in compliance with the License.  
# A copy of the License is located at  
#  
# http://aws.amazon.com/asl/  
#  
# or in the "license" file accompanying this file.  
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, express or implied.  
# See the License for the specific language governing permissions and
limitations under the License.  
#  
# Modified  
FROM
amazonlinux:latest@sha256:7f12c425c74940d60c035daa77c34696bb961d8ebc81fd7897f4dedf696656cd  
  
RUN yum install python27-pip -y && yum clean all \  
&& rm -rf /var/cache/yum \  
&& pip install virtualenv --no-cache-dir  
  
RUN set -x && \  
# Install docker-compose  
# https://docs.docker.com/compose/install/  
DOCKER_COMPOSE_URL=https://github.com$(curl -L
https://github.com/docker/compose/releases/latest | grep -Eo
'href="[^"]+docker-compose-Linux-x86_64' | sed 's/^href="//' | head -1) && \  
curl -Lo /usr/local/bin/docker-compose $DOCKER_COMPOSE_URL && \  
chmod a+rx /usr/local/bin/docker-compose && \  
\  
# Basic check it works  
docker-compose version \  
&& rm -rf /tmp/* /var/tmp/*  
  
VOLUME /var/lib/docker  
  
COPY dockerd-entrypoint.sh /usr/local/bin/  
  
ENV PATH="/usr/local/bin:$PATH"  
CMD ["python"]  
  
ENTRYPOINT ["dockerd-entrypoint.sh"]  

