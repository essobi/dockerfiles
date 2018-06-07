# Copyright 2015 Guillaume Pellerin  
# Copyright 2015 Thomas Fillon  
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
FROM parisson/timeside:latest-dev  
  
MAINTAINER Guillaume Pellerin <yomguy@parisson.com>, Thomas Fillon
<thomas@parisson.com>  
  
RUN mkdir -p /srv/src/timeside-diadems  
WORKDIR /srv/src/timeside-diadems  
  
# Install binary dependencies with conda  
ADD conda-requirements.txt /srv/src/timeside-diadems/  
  
RUN conda install -c conda-forge --file conda-requirements.txt  
  
# Install remaining depencies with pip  
ADD requirements.txt /srv/src/timeside-diadems/  
RUN pip install -r requirements.txt  
  
# Clone and install app  
ADD . /srv/src/timeside-diadems/  
RUN pip install -e .  
  
WORKDIR /srv/app  
EXPOSE 8000  

