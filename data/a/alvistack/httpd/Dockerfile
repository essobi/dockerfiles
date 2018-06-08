# (c) Wong Hoi Sing Edison <hswong3i@pantarei-design.com>  
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
FROM httpd:2.4  
VOLUME /var/www/html  
WORKDIR /var/www/html  
  
EXPOSE 80  
ENTRYPOINT [ "dumb-init", "--" ]  
CMD [ "/usr/local/apache2/bin/httpd", "-DFOREGROUND" ]  
  
# Prepare APT depedencies  
RUN set -ex \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y curl patch \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install dumb-init  
RUN set -ex \  
&& curl -skL https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64 > /usr/local/bin/dumb-init \  
&& chmod 0755 /usr/local/bin/dumb-init  
  
# Copy files  
COPY files /  
  
# Apply patches  
RUN set -ex \  
&& patch -d/ -p1 < /.patch  
  
# Ensure required folders exist with correct owner:group  
RUN set -ex \  
&& rm -rf /usr/local/apache2/conf/extra/*.conf \  
&& mkdir -p /var/www/html \  
&& chown -Rf www-data:www-data /var/www/html \  
&& chmod 0755 /var/www/html  
  

