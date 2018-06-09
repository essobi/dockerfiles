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
FROM ubuntu:12.04  
MAINTAINER Stock Software  
  
ENV CHEF_VERSION=11.1.7  
RUN apt-get update -q --yes && \  
apt-get install -q --yes git curl build-essential libxml2-dev libxslt1-dev
runit -y && \  
curl -L https://packages.chef.io/stable/ubuntu/12.04/chef-
server_${CHEF_VERSION}-1_amd64.deb > /tmp/chef-server.deb && \  
dpkg -i /tmp/chef-server.deb && \  
/opt/chef-server/embedded/bin/gem install knife-backup -v0.0.12 --ignore-
dependencies && \  
rm -f /tmp/chef-server.deb && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*  
  
ADD chef-server.rb /etc/chef-server/chef-server.rb  
ADD chef-server.rb ${HOME}/.chef/chef-server.rb  
ADD init.rb /init.rb  
ADD backup.rb /opt/chef-server/embedded/bin/backup  
  
RUN chmod u+x /opt/chef-server/embedded/bin/backup  
  
VOLUME /opt/chef-server/backups  
  
EXPOSE 80 443  
CMD [ "/opt/chef-server/embedded/bin/ruby", "/init.rb" ]  

