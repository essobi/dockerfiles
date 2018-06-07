FROM ubuntu:16.04  
MAINTAINER didstopia  
  
# Run a quick apt-get update/upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get update &&
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y &&
DEBIAN_FRONTEND=noninteractive apt-get autoremove -y --purge  
  
# Install dependencies, mainly for SteamCMD  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
ca-certificates \  
software-properties-common \  
python-software-properties \  
libasound2 \  
xorg-dev \  
libx11-6 \  
libxcursor1 \  
libxinerama1 \  
libxrandr2 \  
libxi6 \  
libgl1-mesa-dev \  
curl \  
wget  
  
# Run as root  
USER root  
  
# Setup the default timezone  
ENV TZ=Europe/Helsinki  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Setup the volume  
RUN mkdir -p /factorio/saves  
VOLUME ["/factorio/saves"]  
  
# Install Factorio  
RUN wget -q --show-progress --no-check-certificate
https://www.factorio.com/get-download/0.12.35/headless/linux64 -O
/factorio.tar.gz && \  
tar -xzf /factorio.tar.gz -C / && \  
chmod +x /factorio/bin/x64/factorio && \  
rm -fr /factorio.tar.gz  
  
# Copy the Factorio script  
ADD start_factorio.sh /start.sh  
ADD check_autosave.sh /check_autosave.sh  
  
# Expose necessary ports  
EXPOSE 34197/udp  
  
# Setup default environment variables for the server  
ENV FACTORIO_WORLD_NAME "docker"  
ENV FACTORIO_AUTOSAVE_INTERVAL "5"  
ENV FACTORIO_LATENCY_MS "250"  
ENV FACTORIO_NO_AUTO_PAUSE "0"  
# Cleanup  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean &&
DEBIAN_FRONTEND=noninteractive apt-get clean  
  
# Start the server  
ENTRYPOINT ["./start.sh"]  

