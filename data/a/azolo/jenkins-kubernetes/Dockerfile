FROM jenkins/jenkins:lts-alpine  
  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/  
ENV JAVA_OPTS="-XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAMFraction=1 -XshowSettings:vm"  
ENV TRY_UPGRADE_IF_NO_MARKER=true  
  
RUN /usr/local/bin/install-plugins.sh blueocean kubernetes github slack
matrix-auth amazon-ecr  

