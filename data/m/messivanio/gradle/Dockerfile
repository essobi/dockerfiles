FROM openjdk:7u111-jdk  
  
# Gradle  
ENV GRADLE_VERSION 2.4  
ENV GRADLE_SHA
c4eaecc621a81f567ded1aede4a5ddb281cc02a03a6a87c4f5502add8fc2f16f  
  
RUN cd /usr/lib \  
&& curl -fl
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
gradle-bin.zip \  
&& echo "$GRADLE_SHA gradle-bin.zip" | sha256sum -c - \  
&& unzip "gradle-bin.zip" \  
&& ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle \  
&& rm "gradle-bin.zip"  
  
# Set Appropriate Environmental Variables  
ENV GRADLE_HOME /usr/lib/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Caches  
VOLUME ["/root/.gradle/caches", "/usr/bin/app"]  
  
# Default command is "/usr/bin/gradle -version" on /usr/bin/app dir  
# (ie. Mount project at /usr/bin/app "docker --rm -v /path/to/app:/usr/bin/app
gradle <command>")  
WORKDIR /usr/bin/app  
ENTRYPOINT ["gradle"]  
CMD ["-version"]  

