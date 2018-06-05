FROM codenvy/ubuntu_android  
ENV GRADLE_VERSION=2.10  
ENV GRADLE_HOME=/home/user/gradle-$GRADLE_VERSION  
ENV PATH=$GRADLE_HOME/bin:$PATH  
  
RUN wget -P /home/user/ \--quiet
https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip && \  
cd /home/user/ && unzip gradle-$GRADLE_VERSION-bin.zip && rm
gradle-$GRADLE_VERSION-bin.zip  
  
RUN echo y | $ANDROID_HOME/tools/android \--silent update sdk \--all \--no-ui
\--filter addon-google_apis-google-21,extra-android-m2repository,addon-
google_apis-google-22,android-22,build-tools-22.0.1,addon-google_apis-
google-24,build-tools-24.0.1,android-24 && \  
cd /home/user/ && \  
git clone \--depth 1 https://github.com/mosabua/maven-android-sdk-deployer.git
\--quiet && \  
cd maven-android-sdk-deployer && \  
mvn install \--quiet -P 5.0 && \  
rm -rf /home/user/maven-android-sdk-deployer && \  
echo "done!"

