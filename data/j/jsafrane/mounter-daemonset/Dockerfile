# Copyright 2017  
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
# This is a simple container image that has utilities for NFS, Gluster and
Ceph  
# and runs a minimal init that reaps zombies.  
FROM fedora:27  
RUN yum -y install hostname glusterfs-client busybox nfs-utils ceph-common
iscsi-initiator-utils && yum clean all  
# for debugging  
RUN yum -y install net-tools procps-ng psmisc && yum clean all  
  
RUN mv /etc/iscsi /etc/iscsi-save  
COPY inittab /etc/  
COPY rc.local /etc/rc.d/  
COPY register-mount-container /usr/bin  
  
ENTRYPOINT ["busybox", "init"]  

