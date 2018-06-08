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
FROM vpgrp/ubuntu:xenial  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
TZ="Europe/Amsterdam"  
RUN curl --location --silent \  
"https://packages.microsoft.com/keys/microsoft.asc" | \  
apt-key --keyring /etc/apt/trusted.gpg.d/microsoft-keyring.gpg add \- && \  
echo "deb https://packages.microsoft.com/ubuntu/16.04/prod xenial main" > \  
/etc/apt/sources.list.d/microsoft.list && \  
apt-get update -qq && \  
apt-get upgrade -qq -y && \  
apt-get install -qq -y \  
libcurl3 \  
liblttng-ust0 \  
libicu55 \  
libssl1.0.0 \  
libunwind8 \  
powershell && \  
apt-clean  
  
CMD [ "/usr/bin/pwsh" ]  
# EOF  

