# Copyright 2016 Matthias Neugebauer All rights reserved.  
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
FROM ubuntu:latest  
MAINTAINER Matthias Neugebauer <mtneug@mailbox.org>  
  
RUN groupadd \  
\--gid 1000 \  
user \  
&& useradd \  
\--uid 1000 \  
\--gid 1000 \  
\--create-home \  
user \  
&& apt-get update \  
&& apt-get install -y \  
texlive-full \  
inotify-tools \  
python-pygments \  
pandoc \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY build.sh /build.sh  
  
USER user  
WORKDIR /doc  
VOLUME [ "/doc" ]  
  
ENTRYPOINT [ "/build.sh" ]  
CMD []  

