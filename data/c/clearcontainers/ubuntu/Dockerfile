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
# Ubuntu Sandbox for Clear Containers  
FROM ubuntu:16.04  
# Ensure packages are current, then install dependencies  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y vim procps wget libmnl0  
  
# Install Docker  
RUN apt-get install -y apt-transport-https ca-certificates curl software-
properties-common  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable"  
RUN apt-get update  
RUN apt-get install -y docker-ce  
  
# Add the OBS repository  
RUN sh -c "echo 'deb
http://download.opensuse.org/repositories/home:/clearlinux:/preview:/clear-
containers-2.1/xUbuntu_16.04/ /' >> /etc/apt/sources.list.d/cc-oci-
runtime.list"  
  
# Install OBS key  
RUN wget
http://download.opensuse.org/repositories/home:clearlinux:preview:clear-
containers-2.1/xUbuntu_16.04/Release.key  
RUN apt-key add Release.key  
RUN rm Release.key  
  
# Install the Clear Containers assets.  
RUN apt-get update  
# Returning `true` since the installation of cc-oci-runtime  
# tries to start cc-proxy socket via systemd and returns an  
# error since we do not have systemd inside the container.  
# We will start cc-proxy later.  
RUN apt-get install -y cc-oci-runtime || true  
  
# Have Docker run with Clear Containers as the default runtime  
RUN echo "#!/bin/bash\ndockerd --add-runtime cor=/usr/bin/cc-oci-runtime \  
\--default-runtime=cor --storage-driver=vfs > \  
/dev/null 2>&1 &\n/usr/libexec/cc-proxy &" > \  
/root/start-cc.sh && chmod +x /root/start-cc.sh  
  
ENV HOME /root  
WORKDIR $HOME  
  
# Use Clear Containers by default  
CMD bash -C '/root/start-cc.sh';'bash'  

