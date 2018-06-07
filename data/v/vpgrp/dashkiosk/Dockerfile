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
FROM vpgrp/nodejs:latest  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
TZ="Europe/Amsterdam"  
RUN apt-get update -qq && \  
apt-get upgrade -qq -y && \  
apt-get install -qq -y \  
python \  
build-essential \  
libavahi-compat-libdnssd-dev && \  
apt-clean  
  
RUN git clone https://github.com/vp-noc/dashkiosk \  
/opt/dashkiosk && \  
rm /opt/dashkiosk/app/images/unassigned/*.jpg  
  
ADD files /  
  
RUN cd /opt/dashkiosk && \  
git checkout vente-privee-branding && \  
npm --loglevel=error install --global bower grunt-cli && \  
npm --loglevel=error install && \  
grunt  
  
EXPOSE 8080  
ENV db__options__storage /opt/dashkiosk/db/dashkiosk.sqlite  
  
WORKDIR /opt/dashkiosk  
  
ENTRYPOINT [ "/usr/bin/node", "/opt/dashkiosk/dist/server.js" ]  
  
CMD [ "--environment", "production", "--port", "8080", "--branding", "vente-
privee" ]  
# EOF  

