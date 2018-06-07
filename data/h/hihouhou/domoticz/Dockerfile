#  
# Domoticz Dockerfile  
#  
# https://github.com/  
#  
# Pull base image.  
FROM debian:latest  
  
MAINTAINER hihouhou < hihouhou@hihouhou.com >  
  
# Update & install packages  
RUN apt-get update && \  
apt-get install -y python3-dev cmake wget git libssl-dev build-essential
libboost-dev libboost-thread-dev libboost-system-dev libsqlite3-dev curl
libcurl4-openssl-dev libusb-dev zlib1g-dev  
  
# Download & deploy domoticz  
RUN git clone https://github.com/domoticz/domoticz.git domoticz  
RUN cd domoticz && cmake -DCMAKE_BUILD_TYPE=Release .  
RUN cd domoticz && make -j 3  
  
EXPOSE 8080  
CMD ["/domoticz/domoticz", "-www 8080"]  

