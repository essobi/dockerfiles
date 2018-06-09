# Copyright (c) 2017, Intel Corporation  
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
FROM intelonp/centos-source-openstack-base:0018  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /tempest-source && git clone git://github.com/redhat-
openstack/tempest.git /tempest-source/tempest && pushd /tempest-source/tempest
&& git checkout aaff550edab124a744b2888bcf7a7d70d3abfa0c && popd  
  
# NOTE(Jeffrey4l): remove the tempest version constraint in the  
# upper-constrains.txt file. Otherwise, it will be failed.  
RUN ln -s tempest-source/* tempest \  
&& sed -i 's/^tempest===.*$//' requirements/upper-constraints.txt \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /tempest \  
&& mkdir -p /etc/tempest /var/log/tempest /etc/tempest/tempest_lock  
  
WORKDIR /tempest  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
RUN chmod 755 /usr/local/bin/kolla_extend_start  
  

