FROM buildpack-deps:xenial-curl  
MAINTAINER David Manouchehri  
  
RUN apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-common
apt-transport-https && \  
curl -fsSL https://dl.winehq.org/wine-builds/Release.key | apt-key add - && \  
dpkg --add-architecture i386 && \  
add-apt-repository https://dl.winehq.org/wine-builds/ubuntu/ && \  
apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install --install-recommends winehq-
stable  
  
RUN useradd -m wine  
USER wine  
WORKDIR /home/wine  
ENV HOME /home/wine  
  
CMD ["/bin/bash"]  

