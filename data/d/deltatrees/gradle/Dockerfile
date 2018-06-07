FROM java:openjdk-8u66-jdk  
  
RUN apt-get update && apt-get upgrade -y && apt-get clean  
  
# Gradle  
ENV GRADLE_VERSION 2.8  
ENV GRADLE_HASH 0898dd55c99a188cb9ff06b4460c96c3  
WORKDIR /opt  
RUN wget -q
"https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"
&& \  
echo "${GRADLE_HASH} gradle-${GRADLE_VERSION}-bin.zip" >
gradle-${GRADLE_VERSION}-bin.zip.md5 && \  
md5sum -c gradle-${GRADLE_VERSION}-bin.zip.md5 && \  
unzip "gradle-${GRADLE_VERSION}-bin.zip" && \  
ln -s "gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle && \  
rm "gradle-${GRADLE_VERSION}-bin.zip"  
# Set Environmental Variables  
ENV GRADLE_HOME /opt/gradle-${GRADLE_VERSION}  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Caches  
VOLUME /root/.gradle/caches  
  
# Define default command.  
CMD ["bash"]  

