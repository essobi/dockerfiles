# Tools in docker  
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
FROM alpine:3.6  
MAINTAINER Josef Cacek  
  
RUN apk add -U --no-cache bash ruby ruby-io-console ruby-json git py-pip \  
&& apk add -U --no-cache --virtual build_deps \  
build-base ruby-dev libc-dev libffi-dev linux-headers \  
&& gem install travis --no-rdoc --no-ri \  
&& pip install docker-scripts \  
&& apk del build_deps  
  
# Location where travis config stored  
VOLUME /root/.travis  
  
# Generally the current working dir will be used as the repo volume  
VOLUME /repo  
WORKDIR /repo  
  
CMD ["/bin/bash"]  

