FROM yongjhih/ubuntu-jenkins-android  
  
MAINTAINER Andrew Chen <yongjhih@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
RUN echo "y" | android update sdk -u -a --filter platform-tools,extra-android-
support,extra-android-m2repository,extra-google-google_play_services,extra-
google-m2repository,extra-google-analytics_sdk_v2  
  
#RUN find $ANDROID_HOME -type d -exec chmod a+x {} \;  
#RUN chmod -R a+r $ANDROID_HOME  
  
USER jenkins  

