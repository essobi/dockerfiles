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
FROM jenkins:alpine  
  
MAINTAINER Stock Software  
  
ENV JAVA_OPTS=-Djava.awt.headless=true  
  
USER root  
  
RUN apk upgrade --update && \  
apk add --update docker tzdata && \  
cp /usr/share/zoneinfo/Australia/Melbourne /etc/localtime && \  
echo "Australia/Melbourne" > /etc/timezone && \  
apk del tzdata && \  
rm -rf /tmp/* /var/cache/apk/* && \  
addgroup jenkins users  
  
USER jenkins:jenkins  
  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt.override  
COPY plugins.txt /usr/share/jenkins/  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  

