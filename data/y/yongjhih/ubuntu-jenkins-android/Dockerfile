FROM yongjhih/ubuntu-jenkins  
  
MAINTAINER Andrew Chen <yongjhih@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
RUN add-apt-repository ppa:ubuntu-desktop/ubuntu-make  
RUN apt-get update && apt-get install -y ubuntu-make  
  
RUN umake android android-sdk --accept-license
/usr/local/share/umake/android/android-sdk  
  
ENV ANDROID_HOME /usr/local/share/umake/android/android-sdk  
ENV PATH $ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH  
#RUN find $ANDROID_HOME -type d -exec chmod a+x {} \;  
#RUN chmod -R a+r $ANDROID_HOME  
  
USER jenkins  

