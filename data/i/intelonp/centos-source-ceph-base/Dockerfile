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
  
FROM intelonp/centos-source-base:0018  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/ceph \--groups kolla ceph \  
&& mkdir -p /var/lib/ceph \  
&& chown -R 64045:64045 /var/lib/ceph  
  
  
  
  
  
RUN yum -y install ceph ceph-fuse ceph-radosgw parted hdparm btrfs-progs
xfsprogs e2fsprogs && yum clean all  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
RUN chmod 755 /usr/local/bin/kolla_extend_start  
  

