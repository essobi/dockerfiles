# Docker android-build node js image  
  
FROM beevelop/android-nodejs  
MAINTAINER Aneesv <vaneesv@gmail.com>  
  
RUN npm i -g yarn && \  
echo y | android update sdk --no-ui --all \--filter addon-google_apis-
google-25 && \  
echo y | android update sdk --no-ui --all \--filter addon-google_apis-
google-23 && \  
echo y | android update sdk --no-ui --all \--filter addon-google_apis-
google-24 && \  
echo y | android update sdk --no-ui --all \--filter addon-google_apis-
google-22 && \  
echo y | android update sdk --no-ui --all \--filter addon-google_apis-
google-21 && \  
echo y | android update sdk --no-ui --all \--filter build-tools-25.0.0 && \  
echo y | android update sdk --no-ui --all \--filter build-tools-23.0.2 && \  
echo y | android update sdk --no-ui --all \--filter build-tools-23.0.1 && \  
echo y | android update sdk --no-ui --all \--filter build-tools-25.0.2 && \  
echo y | android update sdk --no-ui --all \--filter extra-android-m2repository
&& \  
echo y | android update sdk --no-ui --all \--filter extra-google-m2repository
&& \  
echo y | android update sdk --no-ui --all \--filter extra-google-
google_play_services  

