#The MIT License (MIT)  
#  
#Copyright (c) 2017 Armel Soro  
#  
#Permission is hereby granted, free of charge, to any person obtaining a copy  
#of this software and associated documentation files (the "Software"), to deal  
#in the Software without restriction, including without limitation the rights  
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
#copies of the Software, and to permit persons to whom the Software is  
#furnished to do so, subject to the following conditions:  
#  
#The above copyright notice and this permission notice shall be included in
all  
#copies or substantial portions of the Software.  
#  
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
#SOFTWARE.  
FROM gradle:4.3.1-jdk8-alpine AS BUILD_IMAGE  
MAINTAINER Armel Soro <armel@rm3l.org>  
ARG GRADLE_OPTS="-Dorg.gradle.daemon=false -Dorg.gradle.parallel=false"  
ARG GRADLE_OPTS="$GRADLE_OPTS -Dkotlin.incremental=false
-Dkotlin.compiler.execution.strategy=in-process"  
USER root  
ENV APP_HOME=/code/service-names-port-numbers/  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
COPY . .  
RUN chown -R gradle:gradle $APP_HOME  
USER gradle  
RUN gradle clean build --stacktrace  
  
FROM openjdk:8-jre-alpine  
MAINTAINER Armel Soro <armel@rm3l.org>  
ENV JAVA_OPTS=""  
WORKDIR /root/  
COPY \--from=BUILD_IMAGE \  
/code/service-names-port-numbers/application/build/libs/service-names-port-
numbers-app-0.1.9.jar \  
./service-names-port-numbers-app.jar  
EXPOSE 8080  
EXPOSE 8081  
RUN apk add --no-cache curl  
HEALTHCHECK \--interval=5m --timeout=3s \  
CMD curl -f http://localhost:8081/management/health || exit 1  
VOLUME /etc/rm3l  
ENTRYPOINT exec \  
java \  
$JAVA_OPTS \  
-Djava.security.egd=file:/dev/./urandom \  
-jar /root/service-names-port-numbers-app.jar  

