#  
# Apache License  
# Copyright 2016 ReturnPath  
# Copyright 2016 James Cuzella  
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
##  
## Note: This Docker container and script only automate installation & wrap  
## the original tools released as: "awslabs/amazon-redshift-utils"  
## The source code distributed in this repo is under the Apache License,  
## while the source code provided by Amazon is distributed under the  
## "Amazon Software License": http:aws.amazon.com/asl/  
FROM centos:centos7  
MAINTAINER ReturnPath EFP Core <@ReturnPath>  
  
RUN yum clean all && \  
yum -y install epel-release && \  
yum makecache all && \  
yum -y groups mark convert && \  
yum -y groups mark install "Development Tools" && \  
yum -y groups mark convert "Development Tools" && \  
yum -y groupinstall "Development Tools" && \  
yum -y upgrade glibc nscd && \  
yum -y install libffi-devel openssl-devel && \  
yum -y install git python-pip postgresql postgresql-devel python-devel && \  
pip install --upgrade pip && \  
pip install requests[security] && \  
pip install PyGreSQL wheel && \  
yum -y groupremove "Development tools" && \  
yum -y autoremove && \  
git --version || yum -y install git && \  
yum clean all && rm -rf /var/cache/yum  
  
RUN git clone https://github.com/awslabs/amazon-redshift-utils.git
/opt/amazon-redshift-utils  
ADD ./bin /opt/mega-maid/bin  
RUN chmod +x /opt/mega-maid/bin/*  
#RUN pip install -r /opt/amazon-redshift-utils/src/requirements.txt  
ENV MM_DB_SCHEMA public  
ENV MM_DB_PORT 5439  
ENV MM_OUTPUT_FILE /dev/stdout  
ENV MM_DEBUG True  
ENV MM_IGNORE_ERRORS False  
ENV MM_SLOT_COUNT 2  
ENV MM_MIN_UNSORTED_PCT 5  
ENV MM_MAX_UNSORTED_PCT 50  
ENV MM_DELETED_PCT 15  
ENV MM_STATS_OFF_PCT 10  
ENV MM_MAX_TABLE_SIZE_MB 700*1024  
ENTRYPOINT ["/bin/sh", "-c", "/opt/mega-maid/bin/analyze-vacuum-schema.sh"]  

