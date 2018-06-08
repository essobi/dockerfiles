#FROM java:8-jdk  
FROM isuper/java-oracle  
  
# Gradle  
ENV GRADLE_VERSION 2.13  
ENV GRADLE_SHA
0f665ec6a5a67865faf7ba0d825afb19c26705ea0597cec80dd191b0f2cbb664  
  
RUN apt-get update \  
&& apt-get install unzip \  
&& cd /usr/lib \  
&& curl -fl
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
gradle-bin.zip \  
&& echo "$GRADLE_SHA gradle-bin.zip" | sha256sum -c - \  
&& unzip "gradle-bin.zip" \  
&& ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle \  
&& rm "gradle-bin.zip"  
  
ADD setup.sh /  
  
# Set Appropriate Environmental Variables  
ENV GRADLE_HOME /usr/lib/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Caches  
#VOLUME ["/root/.gradle/caches", "/usr/bin/app"]  
# Default command is "/usr/bin/gradle -version" on /usr/bin/app dir  
# (ie. Mount project at /usr/bin/app "docker --rm -v /path/to/app:/usr/bin/app
gradle <command>")  
#WORKDIR /usr/bin/app  
#ENTRYPOINT ["gradle"]  
#CMD ["-version"]  
CMD ["sh /setup.sh"]  

