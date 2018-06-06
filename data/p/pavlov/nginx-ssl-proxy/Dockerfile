# Copyright 2015 Google Inc. All rights reserved.  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
#you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
FROM nginx  
MAINTAINER Alex Kern <alex@pavlovml.com>  
  
RUN rm /etc/nginx/conf.d/*.conf  
COPY nginx.conf proxy.conf /etc/nginx/  
  
WORKDIR /usr/src  
COPY start.sh .  
  
RUN mkdir -p /tmp/letsencrypt/.well-known/acme-challenge/ && \  
echo "OK" > /tmp/letsencrypt/.well-known/acme-challenge/health  
  
CMD [ "./start.sh" ]  

