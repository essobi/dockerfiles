#  
# Copyright 2015 Red Hat, Inc. and/or its affiliates  
# and other contributors as indicated by the @author tags.  
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
FROM hawkular/docker-maven  
  
USER root  
  
ENV WORKING_DIR=/opt/hawkular-ui-test  
  
RUN yum install -y git wget &&\  
git clone https://github.com/Hawkular-QE/hawkular-ui-test.git ${WORKING_DIR}
&&\  
cd ${WORKING_DIR} &&\  
mvn dependency:go-offline test -Dtest=NoopTest &&\  
ln -s ${WORKING_DIR}/target/surefire-reports /reports &&\  
ln -s ${WORKING_DIR}/docker/hawkular_wait.sh /usr/bin/hawkular_wait.sh &&\  
ln -s ${WORKING_DIR}/docker/docker_start.sh /usr/bin/docker_start.sh  
  
CMD ["sh", "-c", "docker_start.sh"]  

