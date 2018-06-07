# (c) Copyright 2016 Hewlett Packard Enterprise Development LP  
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
# Copyright 2015 Michael Hart (michael.hart.au@gmail.com)  
# https://github.com/mhart/alpine-node  
FROM mhart/alpine-node:6  
ADD scripts/ /scripts/  
ADD assets/ /opt/resource/  
RUN set -ex \  
&& chmod +x /opt/resource/* \  
&& chmod +x /scripts/* \  
&& export NODE_ENV=production \  
&& cd /scripts \  
&& npm install  
ADD LICENSE.txt /usr/share/doc/stackato/LICENSE.txt  

