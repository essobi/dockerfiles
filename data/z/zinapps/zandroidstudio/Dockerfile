FROM zinapps/zvnc  
  
RUN apt-get update; apt-get upgrade -y  
RUN apt-get install software-properties-common unzip wget -y  
RUN apt-get install -y lib32z1 lib32ncurses5 lib32ncurses5-dev lib32stdc++6  
  
RUN add-apt-repository -y ppa:openjdk-r/ppa  
RUN apt-get update  
RUN apt-get install openjdk-8-jdk -y  
  
RUN wget https://dl.google.com/dl/android/studio/ide-zips/2.3.3.0/android-
studio-ide-162.4069837-linux.zip -O sdk.zip  
RUN mv sdk.zip /opt; cd /opt; unzip sdk.zip  
RUN rm /opt/sdk.zip  
  
COPY AndroidStudio.desktop /root/Desktop/AndroidStudio.desktop  
RUN chmod +x /root/Desktop/AndroidStudio.desktop  

