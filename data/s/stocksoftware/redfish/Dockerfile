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
FROM stocksoftware/glassfish:java-8_payara-4.1.1.164  
USER root  
  
ENV JRUBY_JAR=/opt/jruby/jruby-complete-1.7.2.jar \  
GLASSFISH_PATCHER_JAR=/opt/glassfish-domain-patcher/glassfish-domain-
patcher-0.3.jar  
  
ADD http://central.maven.org/maven2/org/jruby/jruby-complete/1.7.2/jruby-
complete-1.7.2.jar ${JRUBY_JAR}  
ADD
http://central.maven.org/maven2/org/realityforge/glassfish/patcher/glassfish-
domain-patcher/0.3/glassfish-domain-patcher-0.3.jar ${GLASSFISH_PATCHER_JAR}  
  
RUN chmod -R a+r ${JRUBY_JAR} ${GLASSFISH_PATCHER_JAR}  
  
USER glassfish:glassfish  

