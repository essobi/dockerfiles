FROM openjdk:8-jdk  
MAINTAINER Rene Ruck <rene@plynk.me>  
  
# Gradle  
ENV GRADLE_VERSION 3.3  
ENV GRADLE_SHA
c58650c278d8cf0696cab65108ae3c8d95eea9c1938e0eb8b997095d5ca9a292  
  
COPY gradle-build.sh /usr/lib/gradle-build.sh  
  
RUN cd /usr/lib \  
&& curl -fl
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
gradle-bin.zip \  
&& echo "$GRADLE_SHA gradle-bin.zip" | sha256sum -c - \  
&& unzip "gradle-bin.zip" \  
&& ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle \  
&& rm "gradle-bin.zip" \  
&& curl -fl https://s3.eu-central-1.amazonaws.com/dynamodb-local-
frankfurt/dynamodb_local_latest.zip -o dynamodb_local_latest.zip \  
&& unzip dynamodb_local_latest.zip -d dynamodb_local_latest \  
&& rm dynamodb_local_latest.zip \  
&& chmod +x /usr/lib/gradle-build.sh \  
&& ln -s /usr/lib/gradle-build.sh /usr/bin/gradle-build \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends python2.7 \  
&& apt-get install -y --no-install-recommends python-setuptools python-pip \  
&& pip install --upgrade pip \  
&& pip install awscli \  
&& wget http://central.maven.org/maven2/io/swagger/swagger-codegen-
cli/2.2.3/swagger-codegen-cli-2.2.3.jar -O swagger-codegen-cli.jar  
  
# Set Appropriate Environmental Variables  
ENV GRADLE_HOME /usr/lib/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Set bogus AWS API keys  
ENV AWS_ACCESS_KEY_ID AAAAAAA  
ENV AWS_SECRET_ACCESS_KEY BBBBBBBBB  
  
# Caches  
VOLUME ["/root/.gradle/caches", "/usr/share/app/"]  
  
# Default command is "/usr/bin/gradle -version" on /usr/share/app dir  
# (ie. Mount project at /usr/share/app "docker --rm -v
/path/to/app:/usr/share/app gradle <command>")  
WORKDIR /usr/share/app  
ENTRYPOINT ["gradle-build"]  
CMD ["-version"]  

