FROM onari/docker-ubuntu1604-node8-ffmpeg-im  
MAINTAINER onari  
  
RUN apt -y install clamav clamav-daemon clamdscan  
RUN freshclam && service clamav-daemon start && service clamav-daemon status  
  

