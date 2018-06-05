FROM ubuntu:artful  
  
LABEL maintainer="Grégory Van den Borre vandenborre.gregory@hotmail.fr"  
  
RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q &&
apt-get -y -q autoclean && apt-get -y -q autoremove)  
RUN apt-get install -y -q wget unzip  
RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q &&
apt-get -y -q autoclean && apt-get -y -q autoremove)  
RUN apt-get install -y -q wget unzip  
RUN wget https://bitbucket.org/yildiz-engine-team/build-application-
binaries/downloads/openjdk_linux-x64.tar.gz  
RUN wget https://bitbucket.org/yildiz-engine-team/build-application-
binaries/downloads/apache-maven.zip  
RUN tar -xzf openjdk_linux-x64.tar.gz  
RUN rm openjdk_linux-x64.tar.gz  
RUN unzip -q apache-maven.zip  
RUN rm apache-maven.zip  
RUN chmod 777 /apache-maven/bin/mvn  
ENV M2_HOME=/apache-maven  
ENV JAVA_HOME=/openjdk_linux-x64  
ENV PATH="${PATH}:${JAVA_HOME}/bin:${M2_HOME}/bin"  
RUN java -version  
RUN mvn -v  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
clean-plugin -Dversion=3.0.0  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
compiler-plugin -Dversion=3.7.0  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
deploy-plugin -Dversion=2.8.2  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
failsafe-plugin -Dversion=2.19.1  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
install-plugin -Dversion=2.5.2  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
resources-plugin -Dversion=3.0.2  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
surefire-plugin -Dversion=2.19.1  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
verifier-plugin -Dversion=1.1  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
jar-plugin -Dversion=3.0.2  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
site-plugin -Dversion=3.6  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
antrun-plugin -Dversion=1.8  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
assembly-plugin -Dversion=3.1.0  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
dependency-plugin -Dversion=3.0.2  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
scm-plugin -Dversion=1.9.5  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
release-plugin -Dversion=2.5.3  
RUN mvn dependency:get -DgroupId=org.sonarsource.scanner.maven
-DartifactId=sonar-maven-plugin -Dversion=3.4.0.905  
RUN mvn dependency:get -DgroupId=com.github.wvengen -DartifactId=proguard-
maven-plugin -Dversion=2.0.14  
RUN mvn dependency:get -DgroupId=com.akathist.maven.plugins.launch4j
-DartifactId=launch4j-maven-plugin -Dversion=1.7.21  
RUN mvn dependency:get -DgroupId=org.jacoco -DartifactId=jacoco-maven-plugin
-Dversion=0.7.9  
RUN mvn dependency:get -DgroupId=org.codehaus.mojo -DartifactId=exec-maven-
plugin -Dversion=1.6.0  
RUN mvn dependency:get -DgroupId=org.sonatype.plugins -DartifactId=nexus-
staging-maven-plugin -Dversion=1.6.8  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
source-plugin -Dversion=3.0.1  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
javadoc-plugin -Dversion=3.0.0  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
gpg-plugin -Dversion=1.6  
RUN mvn dependency:get -DgroupId=org.jooq -DartifactId=jooq-codegen-maven
-Dversion=3.10.0  
RUN mvn dependency:get -DgroupId=org.pitest -DartifactId=pitest-maven
-Dversion=1.2.4  
RUN mvn dependency:get -DgroupId=com.spotify -DartifactId=docker-maven-plugin
-Dversion=1.0.0  
RUN mvn dependency:get -DgroupId=com.spotify -DartifactId=dockerfile-maven-
plugin -Dversion=1.3.6  
RUN mvn dependency:get -DgroupId=org.apache.maven.plugins -DartifactId=maven-
enforcer-plugin -Dversion=1.4.1  
RUN mvn dependency:get -DgroupId=org.owasp -DartifactId=dependency-check-maven
-Dversion=3.0.2  
RUN mvn dependency:get -DgroupId=pl.project13.maven -DartifactId=git-commit-
id-plugin -Dversion=2.2.4  
RUN mvn dependency:get -DgroupId=org.junit.jupiter -DartifactId=junit-jupiter-
api -Dversion=5.0.2  
RUN mvn dependency:get -DgroupId=org.junit.jupiter -DartifactId=junit-jupiter-
engine -Dversion=5.0.2  
RUN mvn dependency:get -DgroupId=org.junit.platform -DartifactId=junit-
platform-launcher -Dversion=1.0.2  
RUN mvn dependency:get -DgroupId=org.junit.platform -DartifactId=junit-
platform-surefire-provider -Dversion=1.0.2  
RUN mvn dependency:get -DgroupId=org.sonatype.plexus -DartifactId=plexus-
cipher -Dversion=1.7  
RUN mvn dependency:get -DgroupId=org.apache.httpcomponents
-DartifactId=httpclient -Dversion=4.3.5  
RUN mvn dependency:get -DgroupId=commons-beanutils -DartifactId=commons-
beanutils-core -Dversion=1.8.3  
RUN mvn dependency:get -DgroupId=com.intellij -DartifactId=annotations
-Dversion=9.0.4  
RUN mvn dependency:get -DgroupId=org.slf4j -DartifactId=slf4j-api
-Dversion=1.7.7  
RUN mvn dependency:get -DgroupId=logkit -DartifactId=logkit -Dversion=1.0.1  
RUN mvn dependency:get -DgroupId=avalon-framework -DartifactId=avalon-
framework -Dversion=4.1.3  
RUN mvn dependency:get -DgroupId=org.codehaus.mojo -DartifactId=build-helper-
maven-plugin -Dversion=3.0.0  
RUN mvn dependency:get -DgroupId=org.codehaus.mojo -DartifactId=versions-
maven-plugin -Dversion=2.5  
  
RUN mkdir /src  
WORKDIR /src  
  

