FROM beevelop/ionic  
RUN apt-get update  
RUN apt-get install git -y  
RUN cordova telemetry off  
CMD bash -c "git clone https://github.com/lupin012345/SugarizerOS.git;cd
SugarizerOS;sh install.sh;cp sugar-
cordova/platforms/android/build/outputs/apk/android-debug.apk /output/android-
debug.apk"

