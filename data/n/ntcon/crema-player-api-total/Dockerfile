FROM java:8-jdk  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
COPY ./ /usr/src/player-api  
  
# Gradle  
ENV GRADLE_VERSION 2.6  
ENV GRADLE_HASH 88a116b028e4749c9d77e514904755a9  
WORKDIR /usr/bin  
RUN wget
"https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"
&& \  
echo "${GRADLE_HASH} gradle-${GRADLE_VERSION}-bin.zip" >
gradle-${GRADLE_VERSION}-bin.zip.md5 && \  
md5sum -c gradle-${GRADLE_VERSION}-bin.zip.md5 && \  
unzip "gradle-${GRADLE_VERSION}-bin.zip" && \  
ln -s "gradle-${GRADLE_VERSION}" gradle && \  
rm "gradle-${GRADLE_VERSION}-bin.zip" && \  
mkdir -p /usr/src/app  
  
# Set Appropriate Environmental Variables  
ENV GRADLE_HOME /usr/bin/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
ENV CLASSPATH /root/.gradle/caches/modules-2/files-2.1  
WORKDIR /usr/src/player-api  
VOLUME /var/log/caffe/crema  
  
RUN gradle exportJar  
  
CMD java -jar build/libs/player-api-1.0-SNAPSHOT-fat.jar

