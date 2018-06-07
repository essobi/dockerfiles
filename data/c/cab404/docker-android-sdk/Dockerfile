FROM ubuntu  
LABEL maintainer="cab404 <me@cab404.ru>"  
# Lets hope we'll get that instruction in future  
# TAG android-sdk  
  
ARG SDK_URL=https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip  
  
WORKDIR /usr/local/asdk  
  
# installing all required things  
RUN apt-get update -y  
RUN apt-get install -y unzip wget openjdk-8-jdk-headless  
  
ENV ANDROID_HOME=/usr/local/asdk  
ENV PATH=$PATH:/usr/local/asdk/tools/bin  
  
# and now downloading and updating sdk  
RUN \  
wget "$SDK_URL" -O asdk.zip; \  
unzip asdk.zip; \  
rm asdk.zip;  
  
# removing now unrequired things  
RUN apt-get remove -y unzip wget;  
RUN apt-get autoclean  
RUN yes | sdkmanager --licenses  
  
ONBUILD RUN yes | sdkmanager --update  
ONBUILD RUN yes | sdkmanager --licenses  

