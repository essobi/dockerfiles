FROM java:8  
MAINTAINER Heribert Hirth "docker@frostcode.de"  
# install Git and unzip  
RUN apt-get install -q -y git unzip  
  
# install Maven  
ENV MAVEN_VERSION 3.2.5  
ENV M2_HOME /opt/maven  
ENV M2 $M2_HOME/bin  
ENV MAVEN_OPTS -Xms256m -Xmx512m  
ENV PATH $M2:$PATH  
ADD http://apache.openmirror.de/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz /tmp/  
RUN mkdir -p $M2_HOME  
RUN tar -xzf /tmp/apache-maven-$MAVEN_VERSION-bin.tar.gz -C $M2_HOME/ --strip
1  
RUN rm /tmp/apache-maven-$MAVEN_VERSION-bin.tar.gz  
  
# install Gradle  
ENV GRADLE_VERSION 2.3  
ENV GRADLE_HOME /opt/gradle  
ENV PATH $GRADLE_HOME/bin:$PATH  
ADD https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip
/tmp/  
RUN unzip -q /tmp/gradle-$GRADLE_VERSION-bin.zip -d /opt/  
RUN mv /opt/gradle-$GRADLE_VERSION $GRADLE_HOME  
RUN chmod u+x $GRADLE_HOME/bin/gradle  
RUN rm /tmp/gradle-$GRADLE_VERSION-bin.zip  
  
# install Android SDK and build packages  
ENV ANDROID_SDK_VERSION r24.1.2  
ENV ANDROID_BUILD_TOOLS_VERSION 22.0.1  
ENV ANDROID_HOME /opt/android  
RUN apt-get update  
RUN apt-get install -q -y lib32z1 lib32ncurses5 lib32stdc++6  
ADD http://dl.google.com/android/android-sdk_$ANDROID_SDK_VERSION-linux.tgz
/tmp/  
RUN mkdir -p $ANDROID_HOME  
RUN tar -xzf /tmp/android-sdk_$ANDROID_SDK_VERSION-linux.tgz -C $ANDROID_HOME/
-o  
RUN rm /tmp/android-sdk_$ANDROID_SDK_VERSION-linux.tgz  
ENV PATH $PATH:$ANDROID_HOME/android-sdk-linux/tools:$ANDROID_HOME/android-
sdk-linux/platform-tools  
# android list sdk --all --extended  
RUN echo y | $ANDROID_HOME/android-sdk-linux/tools/android update sdk --filter
platform-tools,build-tools-$ANDROID_BUILD_TOOLS_VERSION,android-22,sys-
img-x86-android-22 --no-ui --force -a  
  
# create Android emulator  
# RUN echo n | android create avd --force --device "Nexus 5" --name test
--target android-22 --abi x86 --skin WVGA800 --sdcard 512M  
# install Jenkins  
ADD http://mirrors.jenkins-ci.org/war-stable/latest/jenkins.war /opt/  
RUN chmod 644 /opt/jenkins.war  
ENV JENKINS_HOME /var/jenkins  
ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]  
EXPOSE 8080  
CMD [""]

