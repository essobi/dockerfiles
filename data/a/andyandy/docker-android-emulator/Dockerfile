FROM andyandy/android-ci:latest  
MAINTAINER Andreas Häber <andreas.haber@intele.com>  
  
# Install all dependencies  
RUN apt-get update && \  
apt-get install -y redir && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Expose android port  
EXPOSE 5555  
# VNC port  
EXPOSE 5900  
# Needed to be able to run VNC - bug of Android SDK  
RUN mkdir ${ANDROID_HOME}/tools/keymaps && touch
${ANDROID_HOME}/tools/keymaps/en-us  
  
# Add start script  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
# Add wait-for-emulator script  
ADD android-wait-for-emulator.sh /wait-for-emulator.sh  
RUN chmod +x /wait-for-emulator.sh  
  
# Install dependencies for emulator  
RUN echo y | android update sdk --no-ui --all -t `android list sdk --all|grep
"SDK Platform Android 4.3.1, API 18"|awk -F'[^0-9]*' '{print $2}'` && \  
echo y | android update sdk --no-ui --all --filter sys-img-
armeabi-v7a-android-18 --force && \  
echo y | android update sdk --no-ui --all --filter sys-img-x86-android-18
--force  
  
# Create emulators  
RUN echo n | android create avd --force -n "x86" -t android-18 --abi
default/x86  
RUN echo n | android create avd --force -n "arm" -t android-18 --abi
default/armeabi-v7a  

