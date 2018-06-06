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
# Fedora Sandbox for Clear Containers  
FROM fedora:latest  
  
MAINTAINER Samuel Ortiz "samuel.ortiz@intel.com"  
RUN dnf update -y  
RUN dnf install -y 'dnf-command(config-manager)' 'dnf-plugins-core'  
  
# Install the Clear Containers and docker fedora repos  
RUN dnf config-manager --add-repo
http://download.opensuse.org/repositories/home:clearlinux:preview:clear-
containers-2.1/Fedora\\_25/home:clearlinux:preview:clear-containers-2.1.repo  
RUN dnf config-manager --add-repo
https://download.docker.com/linux/fedora/docker-ce.repo  
  
# Install repos public keys  
RUN rpm --import
http://download.opensuse.org/repositories/home:/clearlinux:/preview:/clear-
containers-2.1/Fedora_25/repodata/repomd.xml.key  
RUN rpm --import https://download.docker.com/linux/fedora/gpg  
  
# Install Clear Containers and the docker packages  
RUN dnf install -y cc-oci-runtime linux-container docker-ce procps vim  
  
# Have Docker run with Clear Containers as the default runtime  
RUN echo -e "#!/bin/bash\ndockerd --add-runtime cor=/usr/bin/cc-oci-runtime \  
\--default-runtime=cor --storage-driver=vfs > \  
/dev/null 2>&1 &\n/usr/libexec/cc-proxy &" > \  
/root/start-cc.sh && chmod +x /root/start-cc.sh  
  
ENV HOME /root  
WORKDIR $HOME  
  
# Use Clear Containers by default  
CMD bash -C '/root/start-cc.sh';'bash'  

