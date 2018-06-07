FROM maven:3.3.9-jdk-8-alpine  
MAINTAINER Sebastian Hoß (mail@shoss.de)  
  
# TODO: https://github.com/docker/hub-feedback/issues/292  
# TODO: https://github.com/docker/hub-feedback/issues/403  
RUN mkdir -p /mbp && \  
mkdir -p /config && \  
mkdir -p /repository && \  
mkdir -p /project && \  
mkdir -p /workspace  
  
VOLUME /project  
  
COPY build/docker/local-nexus-mirror.xml /config/  
COPY build/docker/google-mirror.xml /config/  
  
COPY pom.xml /mbp/  
COPY maven-parents/pom.xml /mbp/maven-parents/  
COPY maven-parents/maven-parents-superpom/pom.xml /mbp/maven-parents/maven-
parents-superpom/  
COPY maven-parents/maven-parents-java/pom.xml /mbp/maven-parents/maven-
parents-java/  
COPY maven-parents/maven-parents-java/pom.xml /mbp/maven-parents/maven-
parents-java/  
COPY maven-parents/maven-parents-java/pom.xml /mbp/maven-parents/maven-
parents-java/  
COPY maven-parents/maven-parents-java/maven-parents-java-prototype/pom.xml
/mbp/maven-parents/maven-parents-java/maven-parents-java-prototype/  
COPY maven-parents/maven-parents-java/maven-parents-java-stable/pom.xml
/mbp/maven-parents/maven-parents-java/maven-parents-java-stable/  
COPY maven-boms/pom.xml /mbp/maven-boms/  
COPY maven-boms/maven-boms-all/pom.xml /mbp/maven-boms/maven-boms-all/  
COPY maven-boms/maven-boms-aspect/pom.xml /mbp/maven-boms/maven-boms-aspect/  
COPY maven-boms/maven-boms-bytecode/pom.xml /mbp/maven-boms/maven-boms-
bytecode/  
COPY maven-boms/maven-boms-cache/pom.xml /mbp/maven-boms/maven-boms-cache/  
COPY maven-boms/maven-boms-camel/pom.xml /mbp/maven-boms/maven-boms-camel/  
COPY maven-boms/maven-boms-database/pom.xml /mbp/maven-boms/maven-boms-
database/  
COPY maven-boms/maven-boms-eclipse/pom.xml /mbp/maven-boms/maven-boms-eclipse/  
COPY maven-boms/maven-boms-google/pom.xml /mbp/maven-boms/maven-boms-google/  
COPY maven-boms/maven-boms-javax/pom.xml /mbp/maven-boms/maven-boms-javax/  
COPY maven-boms/maven-boms-json/pom.xml /mbp/maven-boms/maven-boms-json/  
COPY maven-boms/maven-boms-karaf/pom.xml /mbp/maven-boms/maven-boms-karaf/  
COPY maven-boms/maven-boms-maven/pom.xml /mbp/maven-boms/maven-boms-maven/  
COPY maven-boms/maven-boms-pax/pom.xml /mbp/maven-boms/maven-boms-pax/  
COPY maven-boms/maven-boms-scripting/pom.xml /mbp/maven-boms/maven-boms-
scripting/  
COPY maven-boms/maven-boms-sebhoss/pom.xml /mbp/maven-boms/maven-boms-sebhoss/  
COPY maven-boms/maven-boms-square/pom.xml /mbp/maven-boms/maven-boms-square/  
COPY maven-boms/maven-boms-testing/pom.xml /mbp/maven-boms/maven-boms-testing/  
COPY maven-boms/maven-boms-wikitext/pom.xml /mbp/maven-boms/maven-boms-
wikitext/  
COPY maven-boms/maven-boms-yaml/pom.xml /mbp/maven-boms/maven-boms-yaml/  
  
WORKDIR /mbp  
  
RUN mvn dependency:go-offline \  
-Dmaven.repo.local=/repository  

