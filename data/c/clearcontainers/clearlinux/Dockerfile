# Copyright (c) 2017 Intel Corporation  
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
#  
# Clear Linux Sandbox for Clear Containers  
FROM clearlinux:latest  
  
MAINTAINER Manohar Castelino "manohar.r.castelino@intel.com"  
#Run swupd multiple time for now so that we upgrade across format bumps  
#This ensures you always have the latest clearlinux image even if the  
#one on dockerhub has not been updated  
#This also works around the overlay file system bug  
#Add a workaround for docker bug https://github.com/moby/moby/issues/31805  
RUN /bin/sh -c 'swupd update; \  
swupd update; \  
swupd update; \  
swupd update; \  
swupd update;'  
  
RUN swupd bundle-add containers-virt  
  
RUN mkdir -p /var/run/ && \  
mkdir -p /etc/docker/ && \  
mkdir -p /run/opencontainer/containers/  
  
RUN echo -e "#!/bin/bash\ndockerd --add-runtime cor=/usr/bin/cc-oci-runtime \  
\--default-runtime=cor --host=unix:///var/run/docker.sock
--host=tcp://0.0.0.0:2375 \  
\--storage-driver=vfs &> /tmp/docker.log &\n/usr/libexec/cc-proxy &" > \  
/root/run_dockerd.sh && chmod +x /root/run_dockerd.sh  
  
ENV HOME /root  
WORKDIR $HOME  
  
# Workaround: Populate Certs on /etc from /var/cache/ca-certs  
RUN /usr/bin/trust-certs  
RUN mkdir -p /etc/ssl  
RUN cd /etc/ssl && ln -s /var/cache/ca-certs certs  
  
CMD bash -C '/root/run_dockerd.sh';'bash'  

