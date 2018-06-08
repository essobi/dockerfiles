#  
# Copyright (c) 2001-2018 Primeton Technologies, Ltd.  
# All rights reserved.  
#  
# author: ZhongWen Li (mailto:lizw@primeton.com)  
#  
FROM primetoninc/jdk:1.8  
ENV GRADLE_VERSION=4.0  
ENV APP_HOME="/app" \  
SERVER_PORT=8080 \  
DEBUG_PORT=8888 \  
DEBUG_ENABLE="no" \  
JAVA_VM_MEM_MIN=512 \  
JAVA_VM_MEM_MAX=1024 \  
PATH=${PATH}:/opt/gradle-${GRADLE_VERSION}/bin  
  
RUN curl --fail --location --retry 3 \  
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \  
-o /tmp/gradle.zip \  
&& unzip /tmp/gradle.zip -d /opt/ \  
&& \rm -f /tmp/gradle.zip  
  
ADD resources/entrypoint.sh ${APP_HOME}/bin/  
  
RUN chmod +x ${APP_HOME}/bin/entrypoint.sh \  
&& mkdir -p ${APP_HOME}/conf \  
&& echo "# Application Configuration directory" > ${APP_HOME}/conf/README.md  
  
ENTRYPOINT ["/bin/bash", "-c", "${APP_HOME}/bin/entrypoint.sh"]  
  
#  
# Prepare for child docker images  
#  
# ONBUILD ADD . /build/  
# ONBUILD RUN cd /build \  
# && gradle check -x test \  
# && gradle clean \  
# && gradle build -x test \  
# && \cp -f build/libs/*.jar ${APP_HOME}/lib/ \  
# && \rm -rf /build ${HOME}/.gradle  

