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
FROM intelonp/centos-source-nova-base:0018  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
  
RUN yum -y install openssh-server && yum clean all  
  
RUN chsh -s /bin/bash nova \  
&& sed -ri
's/session(\s+)required(\s+)pam_loginuid.so/session\1optional\2pam_loginuid.so/'
/etc/pam.d/sshd  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
RUN chmod 755 /usr/local/bin/kolla_extend_start  
  

