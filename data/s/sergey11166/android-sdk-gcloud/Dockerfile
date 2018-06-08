FROM ubuntu:latest  
  
# Update the system  
RUN apt-get update #&& apt-get -y dist-upgrade  
  
# Add requared software  
RUN apt-get -y install unzip openjdk-8-jdk lib32z1 lib32ncurses5 lib32stdc++6
git # requared for android sdk  
RUN apt-get -y install python # requared for gcloud  
RUN apt-get -y install sudo  
  
# Download android sdk  
ADD https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip /opt  
RUN unzip /opt/sdk-tools-linux-4333796.zip -d /opt/android-sdk-linux  
  
ENV PATH=/opt/android-sdk-linux/platform-tools:/opt/android-sdk-
linux/tools:/opt/android-sdk-linux/tools/bin:$PATH  
ENV ANDROID_HOME=/opt/android-sdk-linux  
  
# Adding Android License  
RUN mkdir -p "$ANDROID_HOME/licenses"  
RUN echo "8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/licenses/android-sdk-license"  
  
# Adding /root/.android/repositories.cfg  
RUN mkdir -p $HOME/.android && echo "count=0" >
$HOME/.android/repositories.cfg  
RUN echo y | sdkmanager "extras;google;m2repository"  
  
# Download gcloud  
ENV GCLOUD_TAR=google-cloud-sdk-167.0.0-linux-x86_64.tar.gz  
ADD https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/${GCLOUD_TAR}
/opt/  
RUN tar xzf /opt/${GCLOUD_TAR} -C /opt  
  
# Install the Cloud SDK  
RUN echo y | /opt/google-cloud-sdk/install.sh  
  
ENV PATH=/opt/google-cloud-sdk/bin:$PATH  
  
# Run gcloud init to get started  
RUN echo y | /opt/google-cloud-sdk/bin/gcloud components install beta  
  
# Clean up  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -f /opt/sdk-tools-linux-4333796.zip && \  
rm -f /opt/${GCLOUD_TAR} && \  
apt-get autoremove -y && \  
apt-get clean  

