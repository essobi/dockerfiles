FROM auras/teamcity-agent-android  
  
MAINTAINER Aurelian Dumanovschi <aurasd@gmail.com>  
  
ENV SHELL /bin/bash  
ENV PATH "$ANDROID_HOME/emulator:$ANDROID_HOME/platform-
tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/tools:$PATH"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libpulse0 libx11-6 libgl1-mesa-glx mesa-utils pciutils \  
&& rm -rf /var/lib/apt/lists/*  
  
# Prepare for the emulator  
RUN mkdir $ANDROID_HOME/system-images \  
&& mkdir /home/$USER/.android \  
&& mkdir /home/$USER/.android/avd \  
&& ln -s $ANDROID_HOME/system-images /home/$USER/.android/avd/system-images \  
&& chown -R $USER:$USER $ANDROID_HOME \  
&& chown -R $USER:$USER /home/$USER/.android  
  
# Install the emulator updater.  
ADD emulator-update.sh /emulator-update.sh  
RUN chmod +x /emulator-update.sh  
  
ENTRYPOINT ["/emulator-update.sh"]

