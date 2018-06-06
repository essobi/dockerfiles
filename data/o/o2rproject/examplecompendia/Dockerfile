# (C) Copyright 2016 The o2r project. https://o2r.info  
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
#  
FROM alpine:3.4  
MAINTAINER o2r-project, https://o2r.info  
  
RUN apk add --no-cache \  
curl \  
git \  
bash \  
zip \  
jq \  
&& git clone -b master https://github.com/o2r-project/o2r-bagtainers
/bagtainers \  
&& git clone -b master https://github.com/o2r-project/o2r-muncher /muncher \  
&& cp -r /muncher/test/bagtainers/* /bagtainers \  
&& apk del \  
git \  
&& rm -rf /var/cache /muncher  
  
WORKDIR /bagtainers  
COPY upload_demo_data.sh /upload_demo_data.sh  
  
ENTRYPOINT ["bash", "/upload_demo_data.sh"]  
  
# docker build --tag o2r-upload .

