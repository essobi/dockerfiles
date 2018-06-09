FROM n4nn31355/ubuntu:customuser  
  
USER root  
  
RUN apt-get update && \  
apt-get install -y curl unzip libxext6 libxrender1 libxtst6 libxi6
libfreetype6 openjdk-9-jre lib32z1 lib32ncurses5 lib32stdc++6 && \  
rm -rf /var/lib/apt/lists/*  
RUN curl https://dl.google.com/dl/android/studio/ide-zips/2.3.0.8/android-
studio-ide-162.3764568-linux.zip -o AS.zip  
RUN unzip AS.zip -d /opt && rm AS.zip  
  
USER $CUSTOMUSER  
  
ENV HOME $HOME  
ENV DISPLAY :0  
ENV ANDROID_HOME=$HOME/Android/Sdk  
ENV PATH=$PATH:$ANDROID_HOME/tools  
ENV PATH=$PATH:$ANDROID_HOME/platform-tools  
  
VOLUME $HOME  
  
WORKDIR $HOME  
CMD /opt/android-studio/bin/studio.sh  

