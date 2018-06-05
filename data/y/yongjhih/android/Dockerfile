FROM yongjhih/android:tools  
  
# https://github.com/yongjhih/docker-android/blob/master/ubuntu-
openjdk-8-android-all/Dockerfile  
RUN echo "y" | android update sdk -u -a \--filter android-19 && \  
echo "y" | android update sdk -u -a \--filter build-tools-19.1.0 && \  
echo "y" | android update sdk -u -a \--filter build-tools-19.0.3 && \  
echo "y" | android update sdk -u -a \--filter build-tools-19.0.2 && \  
echo "y" | android update sdk -u -a \--filter build-tools-19.0.1  
  
RUN echo "y" | android update sdk -u -a \--filter android-20 && \  
echo "y" | android update sdk -u -a \--filter build-tools-20.0.0  
  
RUN echo "y" | android update sdk -u -a \--filter android-21 && \  
echo "y" | android update sdk -u -a \--filter build-tools-21.1.2 && \  
echo "y" | android update sdk -u -a \--filter build-tools-21.1.1 && \  
echo "y" | android update sdk -u -a \--filter build-tools-21.1.0 && \  
echo "y" | android update sdk -u -a \--filter build-tools-21.0.2 && \  
echo "y" | android update sdk -u -a \--filter build-tools-21.0.1 && \  
echo "y" | android update sdk -u -a \--filter build-tools-21.0.0  
  
RUN echo "y" | android update sdk -u -a \--filter android-22 && \  
echo "y" | android update sdk -u -a \--filter build-tools-22.0.1 && \  
echo "y" | android update sdk -u -a \--filter build-tools-22.0.0  
  
RUN echo "y" | android update sdk -u -a \--filter android-23 && \  
echo "y" | android update sdk -u -a \--filter build-tools-23.0.3 && \  
echo "y" | android update sdk -u -a \--filter build-tools-23.0.2 && \  
echo "y" | android update sdk -u -a \--filter build-tools-23.0.1 && \  
echo "y" | android update sdk -u -a \--filter build-tools-23.0.0  
  
RUN echo "y" | android update sdk -u -a \--filter extra-android-support && \  
echo "y" | android update sdk -u -a \--filter extra-android-m2repository && \  
echo "y" | android update sdk -u -a \--filter extra-google-
google_play_services && \  
echo "y" | android update sdk -u -a \--filter extra-google-m2repository && \  
echo "y" | android update sdk -u -a \--filter extra-google-analytics_sdk_v2  

