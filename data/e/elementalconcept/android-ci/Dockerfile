FROM r0adkll/android-ci  
MAINTAINER auxx  
  
RUN export GRADLE_USER_HOME="$(pwd)/.gradle"  
RUN export ANDROID_HOME="$(pwd)/.android"  
RUN mkdir -p "${ANDROID_HOME}/licenses"  
RUN echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"${ANDROID_HOME}/licenses/android-sdk-license"  
RUN echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
"${ANDROID_HOME}/licenses/android-sdk-preview-license"  
RUN echo -e "\nd975f751698a77b662f1254ddbeed3901e976f5a" >
"${ANDROID_HOME}/licenses/intel-android-extra-license"  
  
# accepting licences due to bug in pipelines  
RUN echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >>
$ANDROID_HOME/licenses/android-sdk-license  
#RUN echo y | android update sdk --no-ui --all --filter "tool,extra-
android-m2repository,extra-android-support,extra-google-
google_play_services,extra-google-m2repository"  
#RUN echo y | $ANDROID_HOME/tools/bin/sdkmanager
"extras;m2repository;com;android;support;constraint;constraint-layout-
solver;1.0.2"  
COPY assets /opt/docker-assets  
RUN chmod +x /opt/docker-assets/cacher/gradlew  
RUN cd /opt/docker-assets/cacher && ./gradlew tasks  
#RUN cd /opt/docker-assets/cacher && ./gradlew test --no-daemon --parallel  

