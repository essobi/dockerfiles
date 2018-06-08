FROM garethjevans/jenkinsslave-alpine:v1.6  
ENV MAVEN_VERSION 3.5.2  
ENV MAVEN_HOME /opt/maven  
ENV SONAR_VERSION 2.4  
ENV GRADLE_VERSION 2.11  
RUN wget --no-verbose -O /tmp/apache-maven-${MAVEN_VERSION}.tar.gz
http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz && \  
tar xzf /tmp/apache-maven-${MAVEN_VERSION}.tar.gz -C /opt/ && \  
ln -s /opt/apache-maven-${MAVEN_VERSION} ${MAVEN_HOME} && \  
ln -s ${MAVEN_HOME}/bin/mvn /usr/local/bin && \  
rm -f /tmp/apache-maven-${MAVEN_VERSION}.tar.gz  
  
RUN wget http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-
dist/${SONAR_VERSION}/sonar-runner-dist-${SONAR_VERSION}.zip && \  
unzip sonar-runner-dist-${SONAR_VERSION}.zip && \  
mv sonar-runner-${SONAR_VERSION} /opt/sonar-runner  
  
RUN mkdir -p /usr/share/gradle/ && \  
curl -fL
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip -o
/usr/share/gradle/gradle-${GRADLE_VERSION}-all.zip && \  
unzip /usr/share/gradle/gradle-${GRADLE_VERSION}-all.zip -d /usr/share/gradle/
&& \  
rm /usr/share/gradle/gradle-${GRADLE_VERSION}-all.zip && \  
ln -s /usr/share/gradle/gradle-${GRADLE_VERSION}/bin/gradle /usr/local/bin  
  
RUN chown jenkins:jenkins -R /home/jenkins  
  
USER jenkins  
WORKDIR /home/jenkins  

