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
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/mysql \--groups kolla mysql \  
&& mkdir -p /var/lib/mysql \  
&& chown -R 42434:42434 /var/lib/mysql  
  
  
  
  
  
  
RUN yum -y install MariaDB-Galera-server MariaDB-client rsync galera socat
hostname percona-xtrabackup pv tar expect && yum clean all  
COPY mariadb_sudoers /etc/sudoers.d/kolla_mariadb_sudoers  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
COPY security_reset.expect /usr/local/bin/kolla_security_reset  
RUN chmod 755 /usr/local/bin/kolla_extend_start \  
&& chmod 755 /usr/local/bin/kolla_security_reset \  
&& chmod 750 /etc/sudoers.d \  
&& chmod 440 /etc/sudoers.d/kolla_mariadb_sudoers \  
&& rm -rf /var/lib/mysql/*  
  
  
  
  
USER mysql

