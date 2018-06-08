FROM ubuntu:12.04  
  
RUN apt-get update && apt-get install -y wget curl  
RUN apt-get install -y libcurl3 libxqilla6 python python-support  
RUN apt-get install -y libboost-program-options1.48.0 libboost-system1.48.0
libboost-filesystem1.48.0 libboost-regex1.48.0  
  
RUN cd /opt && wget --no-check-certificate
https://annai.egnyte.com/dd/XXBeexrCjA/genetorrent-
common_4.0.0-ubuntu2-12.04_amd64.deb  
RUN cd /opt && wget --no-check-certificate
https://annai.egnyte.com/dd/LHnxNfzkmf/genetorrent-
upload_4.0.0-ubuntu2-12.04_amd64.deb  
RUN cd /opt && wget --no-check-certificate
https://annai.egnyte.com/dd/dQgG3zxoc0/genetorrent-
download_4.0.0-ubuntu2-12.04_amd64.deb  
  
RUN cd /opt && dpkg --install genetorrent-common_4.0.0-ubuntu2-12.04_amd64.deb
genetorrent-upload_4.0.0-ubuntu2-12.04_amd64.deb genetorrent-
download_4.0.0-ubuntu2-12.04_amd64.deb  
  
ADD genetorrent.py /opt/genetorrent.py

