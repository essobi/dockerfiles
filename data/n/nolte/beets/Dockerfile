FROM ubuntu:16.04  
RUN apt-get update && apt-get install software-properties-common -y  
RUN add-apt-repository ppa:flexiondotorg/audio  
RUN apt-get update && apt-get install mp3gain python-dev python-pip python-gi
libgstreamer1.0-0 gstreamer1.0-plugins gstreamer1.0-tools imagemagick python-
rgain libchromaprint-tools ffmpeg libavcodec-extra -y  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install beets==1.3.19  
RUN pip install requests  
RUN pip install pylast  
RUN pip install pyacoustid  
RUN pip install flask  
  
#CMD ["beet"]  

