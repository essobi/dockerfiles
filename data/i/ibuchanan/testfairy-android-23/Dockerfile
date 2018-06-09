FROM ibuchanan/testfairy-android-base  
  
ENV ANDROID_COMPONENTS=platform-tools,build-tools-23.0.2,android-23  
ENV GOOGLE_COMPONENTS=extra-android-m2repository,extra-google-m2repository  
  
RUN echo y | android update sdk --no-ui --all --filter "${ANDROID_COMPONENTS}"
&& \  
echo y | android update sdk --no-ui --all --filter "${GOOGLE_COMPONENTS}"  

