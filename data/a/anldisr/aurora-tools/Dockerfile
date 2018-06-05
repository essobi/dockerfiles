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
# Latest Centos Image.  
FROM centos:latest  
  
# Environments generating user and version.  
ENV AURORA_VERSION 0.20.0-1  
ENV AT_USER aurora  
ENV AT_UID 10141  
ENV HOME /home/$AT_USER  
  
# User creation  
RUN useradd -m -s /bin/bash -N -u ${AT_UID} ${AT_USER} && \  
mkdir -p ${HOME}/.aurora && \  
mkdir -p ${HOME}/aurora/jobs && \  
chown -R ${AT_USER} ${HOME}  
  
# Default clusters.json file  
COPY clusters.json ${HOME}/.aurora/clusters.json  
  
# Update the image and install the aurora-tools rpm from the official bintray
repository  
RUN yum update -y && \  
yum install -y
https://bintray.com/apache/aurora/download_file?file_path=centos-7%2Faurora-
tools-${AURORA_VERSION}.el7.centos.aurora.x86_64.rpm && \  
yum clean all  
  
USER ${AT_USER}  
  
WORKDIR ${HOME}/jobs  

