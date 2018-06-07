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
FROM jboss/keycloak:latest  
  
MAINTAINER Stock Software  
  
ADD changeDatabase.xsl /opt/jboss/keycloak/  
RUN mkdir -p
/opt/jboss/keycloak/modules/system/layers/base/net/sourceforge/jtds/main; cd
/opt/jboss/keycloak/modules/system/layers/base/net/sourceforge/jtds/main; curl
-O
http://central.maven.org/maven2/net/sourceforge/jtds/jtds/1.3.1/jtds-1.3.1.jar  
ADD module.xml
/opt/jboss/keycloak/modules/system/layers/base/net/sourceforge/jtds/main/  
RUN java -jar /usr/share/java/saxon.jar
-s:/opt/jboss/keycloak/standalone/configuration/standalone.xml
-xsl:/opt/jboss/keycloak/changeDatabase.xsl
-o:/opt/jboss/keycloak/standalone/configuration/standalone.xml; java -jar
/usr/share/java/saxon.jar
-s:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml
-xsl:/opt/jboss/keycloak/changeDatabase.xsl
-o:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml; rm
/opt/jboss/keycloak/changeDatabase.xsl  

