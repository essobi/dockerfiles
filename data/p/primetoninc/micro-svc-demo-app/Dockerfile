#  
# Copyright (c) 2001-2018 Primeton Technologies, Ltd.  
# All rights reserved.  
#  
# author: ZhongWen Li (mailto:lizw@primeton.com)  
#  
  
FROM primetoninc/jdk:1.8  
  
ADD . /src/  
  
RUN curl \--fail \--location \--retry 3 \  
https://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz \  
-o /tmp/maven.tar.gz \  
&& tar -zvxf /tmp/maven.tar.gz -C /tmp/ \  
&& cd /src \  
&& /tmp/apache-maven-3.3.9/bin/mvn clean package -Dmaven.test.skip=true
-Dfile.encoding='UTF-8' \  
&& mkdir -p /app/ \  
&& \cp -f /src/micro-svc-app/docker/entrypoint.sh / \  
&& chmod +x /entrypoint.sh \  
&& \mv /src/micro-svc-app/target/micro-svc-app-1.0.0.jar /app/bootstrap.jar \  
&& \rm -rf /tmp/maven.tar.gz /tmp/apache-maven-3.3.9 /tmp/src ${HOME}/.m2  
  
ENV SERVER_PORT=8080 \  
DEBUG_PORT=8888 \  
DEBUG_ENABLE="no" \  
JAVA_VM_MEM_MIN=512 \  
JAVA_VM_MEM_MAX=1024  
  
ENTRYPOINT ["/bin/bash", "-c", "/entrypoint.sh"]  

