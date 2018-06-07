###############################################################################  
# Copyright 2016-2017 Dell Inc.  
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
###############################################################################  
# Consul Docker image for EdgeX Foundry  
FROM consul:0.7.3  
MAINTAINER Cloud Tsai <Cloud.Tsai@Dell.com>  
  
# environment variables  
#ENV CONSUL_LOCAL_CONFIG='{"skip_leave_on_interrupt": true}'  
#Note also Consul team have set skip_leave_on_interrupt using the
CONSUL_LOCAL_CONFIG environment variable. This is recommended for servers and
will be defaulted to true in Consul 0.7 and later, so this will no longer be
necessary.  
  
# kick off Consul with the default argument for EdgeX  
ENTRYPOINT rm -rf /consul/data/* && docker-entrypoint.sh agent -server
-client=0.0.0.0 -bootstrap -ui | tee /edgex/logs/core-consul.log  
CMD []  

