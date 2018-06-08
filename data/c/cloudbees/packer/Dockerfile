FROM ubuntu  
MAINTAINER Alex Soto <asotobueno@cloudbees.com>  
  
#  
# Licensed to the Apache Software Foundation (ASF) under one or more  
# contributor license agreements. See the NOTICE file distributed with  
# this work for additional information regarding copyright ownership.  
# The ASF licenses this file to You under the Apache License, Version 2.0  
# (the "License"); you may not use this file except in compliance with  
# the License. You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
# Install wget and unzip  
RUN apt-get update --yes \  
&& apt-get install --yes curl unzip  
  
# Install Packer  
  
ENV PACKER_BIN_DIR /usr/local/packer/bin  
RUN mkdir --parents $PACKER_BIN_DIR  
  
ENV
PACKER_ZIP=https://releases.hashicorp.com/packer/0.9.0/packer_0.9.0_linux_amd64.zip  
RUN curl -sSLo /tmp/packer.zip $PACKER_ZIP && \  
unzip /tmp/packer.zip -d $PACKER_BIN_DIR && \  
rm /tmp/packer.zip  
  
ENV PATH $PATH:$PACKER_BIN_DIR  
# check that packer is correctly installed  
RUN type packer  
  
# Install Packer Azure  
  
ENV PACKER_AZURE_TAR=https://github.com/Azure/packer-
azure/releases/download/prerelease/packer-azure-linux-amd64-prerelease.tar.gz  
  
RUN curl -sSLo /tmp/packer-azure.tar.gz $PACKER_AZURE_TAR && \  
tar -zxvf /tmp/packer-azure.tar.gz --directory $PACKER_BIN_DIR && \  
rm /tmp/packer-azure.tar.gz  

