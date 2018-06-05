FROM spacecowboy/android-docker-builder:base  
MAINTAINER Jonas Kalderstam <jonas@cowboyprogrammer.org>  
  
# Platform tools first because tools depends on it. Then repositories  
RUN echo y | sdkmanager --update && \  
echo y | sdkmanager "build-tools;23.0.3" \  
"platforms;android-23"  

