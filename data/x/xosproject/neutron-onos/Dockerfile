  
# Copyright 2017-present Open Networking Foundation  
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
# Neutron 'newton' image with ONOS ML2 plugin installed  
  
FROM openstackhelm/neutron:newton  
  
RUN apt update && apt install -y git python-pip && \  
cd /srv && \  
git clone https://github.com/openstack/networking-onos.git -b stable/newton &&
\  
cd networking-onos && \  
python setup.py install && \  
cd /srv && \  
git clone https://github.com/openstack/requirements.git -b stable/newton && \  
sed -i -e 's/neutron-lib===0.4.0/neutron-lib===1.1.0/g' requirements/upper-
constraints.txt && \  
sudo pip install -U -t /var/lib/openstack/lib/python2.7/site-packages/ -c
requirements/upper-constraints.txt neutron-lib && \  
rm -rf networking-onos requirements && \  
rm -rf /var/lib/apt/lists/*  

