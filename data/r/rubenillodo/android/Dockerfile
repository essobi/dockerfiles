FROM openjdk:8  
ENV ANDROID_SDK_HOME /opt/android-sdk  
ENV ANDROID_HOME /opt/android-sdk  
  
RUN apt-get update && \  
apt-get install -y sudo  
  
RUN useradd -u 1000 -m -s /bin/bash -G sudo android && \  
passwd -d android  
  
WORKDIR /opt  
RUN chmod 777 /opt  
USER android  
  
RUN wget -q https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip -O android-sdk.zip && \  
unzip android-sdk.zip -d android-sdk && \  
rm -f android-sdk.zip  
  
ENV PATH ${PATH}:${ANDROID_SDK_HOME}/tools/bin  
  
RUN yes | sdkmanager --licenses  
RUN sdkmanager "tools"  
RUN sdkmanager "extras;google;m2repository"  
RUN sdkmanager "extras;android;m2repository"  
  
WORKDIR /home/android/app  
  
USER root  
RUN chown -R android:android /home/android/app  
USER android  
  
ENTRYPOINT "/bin/bash"  

