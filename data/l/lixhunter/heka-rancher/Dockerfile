#  
# Copyright 2015 Intershop Communications AG.  
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
FROM ianneub/heka:latest  
  
ENV CONFD_VERSION 0.11.0  
ADD
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 /usr/local/bin/confd  
RUN chmod a+x /usr/local/bin/confd  
  
COPY asset/rootfs /  
COPY asset/start.sh /  
  
CMD ["/start.sh"]  

