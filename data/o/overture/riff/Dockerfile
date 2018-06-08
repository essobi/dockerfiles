FROM openjdk:8u121-jdk-alpine  
  
ARG MAVEN_VERSION=3.5.3  
ARG SHA=b52956373fab1dd4277926507ab189fb797b3bc51a2a267a193c931fffad8408  
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries  
  
RUN apk add --no-cache curl tar bash \  
&& mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
&& echo "${SHA} /tmp/apache-maven.tar.gz" | sha256sum -c - \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& rm -f /tmp/apache-maven.tar.gz \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
WORKDIR /usr/src/app  
  
# copy just the pom.xml and install dependencies for caching  
COPY pom.xml .  
RUN mvn verify clean --fail-never  
  
COPY . .  
  
RUN mkdir -p /srv/riff/install \  
&& mkdir -p /srv/riff/exec \  
&& mvn package -Dmaven.test.skip=true \  
&& mv /usr/src/app/target/riff-*-SNAPSHOT.jar /srv/riff/install/RIFF.jar \  
&& mv /usr/src/app/src/main/resources/scripts/run.sh /srv/riff/exec/run.sh  
  
# setup required environment variables  
ENV RIFF_INSTALL_PATH /srv/riff  
  
# start ego server  
WORKDIR $RIFF_INSTALL_PATH  
CMD $RIFF_INSTALL_PATH/exec/run.sh  
  

