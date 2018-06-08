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
FROM openjdk:8-alpine as builder  
  
RUN mkdir /code  
WORKDIR /code  
  
COPY ./gradle/ /code/gradle  
COPY ./build.gradle ./gradle.properties ./gradlew ./settings.gradle /code/  
  
RUN ./gradlew --no-daemon downloadDependencies  
  
COPY ./src/ /code/src  
COPY ./src/main/docker/web.xml /code/src/main/webapp/WEB-INF/web.xml  
  
RUN ./gradlew --no-daemon -Dkotlin.compiler.execution.strategy="in-process"
-Dorg.gradle.parallel=false -Pkotlin.incremental=false war  
  
FROM tomcat:8.5-jre8-alpine  
  
ENV JAVA_OPTS=-Djava.security.egd=file:/dev/urandom  
  
MAINTAINER @blootsvoets  
  
LABEL description="RADAR-CNS Gateway docker container"  
  
COPY \--from=builder /code/build/libs/radar-gateway.war
/usr/local/tomcat/webapps/radar-gateway.war  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

