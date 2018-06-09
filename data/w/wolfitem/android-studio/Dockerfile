FROM wolfitem/baseimage:desktop  
#FROM wolfitem/android-sdk  
MAINTAINER wolfitem <wei.wu86@hotmail.com>  
USER root  
  
RUN apt-get install -y unzip  
RUN curl 'https://dl.google.com/dl/android/studio/ide-zips/1.2.1.1/android-
studio-ide-141.1903250-linux.zip' > /tmp/studio.zip && unzip -d /opt
/tmp/studio.zip && rm /tmp/studio.zip  
  
# Install prerequisites  
RUN apt-get install -y openjdk-7-jdk lib32z1 lib32ncurses5 lib32stdc++6  
# Install other useful tools  
RUN apt-get install -y gradle  
  
#clean up  
RUN apt-get clean  
RUN apt-get purge  
  
#RUN echo ""> 51-android.rules  
#ADD 51-android.rules /etc/udev/rules.d  
#RUN chmod a+r /etc/udev/rules.d/51-android.rules  
USER developer  
  
CMD /opt/android-studio/bin/studio.sh  

