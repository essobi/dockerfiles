FROM debian:stretch  
  
RUN apt-get update && apt-get -y upgrade  
  
RUN apt-get install -y --no-install-recommends libgstreamer1.0-0
gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad
gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc
gstreamer1.0-tools  
  
ADD scripts/ /  

