FROM jenkins/jenkins:2.79  
# add some jenkins plugins  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN xargs /usr/local/bin/install-plugins.sh <
/usr/share/jenkins/ref/plugins.txt  
  
# add docker  
USER root  
  
RUN mkdir -p /tmp/download && \  
curl -L https://get.docker.com/builds/Linux/x86_64/docker-17.05.0-ce.tgz | tar
-xz -C /tmp/download && \  
rm -rf /tmp/download/docker/dockerd && \  
mv /tmp/download/docker/docker* /usr/local/bin/ && \  
rm -rf /tmp/download  
  
RUN groupadd docker  
  
RUN usermod -a -G staff,docker jenkins  
  
USER jenkins  
  
# install Gradle  
RUN \  
cd /usr/local && \  
curl -L https://services.gradle.org/distributions/gradle-4.2-bin.zip -o
gradle-4.2-bin.zip && \  
unzip gradle-4.2-bin.zip && \  
rm gradle-4.2-bin.zip  
  
# export some environment variables  
ENV GRADLE_HOME=/usr/local/gradle-4.2  
ENV PATH=$PATH:$GRADLE_HOME/bin JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
  
# set gradle in jenkins  
COPY add-gradle.groovy /usr/share/jenkins/ref/init.groovy.d/add-gradle.groovy  
  
# set jdk in jenkins  
COPY add-jdk.groovy /usr/share/jenkins/ref/init.groovy.d/add-jdk.groovy  

