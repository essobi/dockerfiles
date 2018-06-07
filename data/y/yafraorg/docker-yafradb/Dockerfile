#  
# Copyright 2015 yafra.org  
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
# yafra.org base docker image  
#  
# source is yafra ubuntu  
FROM yafraorg/docker-yafrabase  
MAINTAINER Yafra <yafraorg@gmail.com>  
  
RUN apk update && \  
apk upgrade  
  
# Install MySQL.  
RUN \  
apk add --update mysql mysql-client perl && \  
sed -i 's/^\\(bind-address\s.*\\)/# \1/' /etc/mysql/my.cnf && \  
sed -i 's/^\\(log_error\s.*\\)/# \1/' /etc/mysql/my.cnf && \  
mkdir /etc/mysql/conf.d && \  
echo "[mysqld]" > /etc/mysql/conf.d/yafra.cnf && \  
echo "lower_case_table_names=1" >> /etc/mysql/conf.d/yafra.cnf && \  
echo "bind-address=0.0.0.0" >> /etc/mysql/conf.d/yafra.cnf  
  
# Install yafra db scripts via git  
RUN \  
mkdir -p /work/repos && \  
cd /work/repos && \  
git clone https://github.com/yafraorg/yafra-database.git  
  
# Define mountable directories.  
#VOLUME ["/etc/mysql", "/var/lib/mysql"]  
VOLUME ["/var/lib/mysql"]  
  
WORKDIR /work/repos/yafra-database  
  
# Expose ports.  
EXPOSE 3306  
CMD ["mysqld_safe"]  

