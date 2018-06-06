#############################################################################
{COPYRIGHT-TOP} ####  
# Copyright 2018 Denilson Nastacio  
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
#############################################################################
{COPYRIGHT-END} ####  
  
FROM python  
  
RUN \  
curl -s https://codeload.github.com/nastacio/clinical-bi/zip/master >
/tmp/clinical-bi.zip && \  
apt-get update && \  
apt-get install unzip && \  
unzip -q /tmp/clinical-bi.zip -d /usr/local && \  
rm /tmp/clinical-bi.zip && \  
apt-get remove unzip -y && \  
pip install --upgrade pip && \  
pip install psycopg2-binary tensorflow pandas configparser  
  
ENTRYPOINT /usr/local/bin/python /usr/local/clinical-bi-
master/src/main/py/ct_estimator.py --database_properties /usr/local/clinical-
bi-master/src/main/py/aact.properties  

