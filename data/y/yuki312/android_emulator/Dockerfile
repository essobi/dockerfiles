# Version 0.0.1  
FROM yuki312/android  
  
MAINTAINER yuki312 <yuki312.m@gmail.com>  
  
# Install android emulator components  
ENV EMULATOR_COMPONENTS addon-google_apis-google-23,sys-img-armeabi-v7a-addon-
google_apis-google-23  
RUN echo y | android update sdk --no-ui --all --filter
"${EMULATOR_COMPONENTS}"  
  
ADD wait_for_emulator.sh /usr/bin/  
RUN chmod +x /usr/bin/wait_for_emulator.sh  

