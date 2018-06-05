################################################################################  
# Dockerfile to build ArchiSteamFarm from source and run it  
# Based on Mono container  
################################################################################  
  
# Set the base image to Mono lastest (4.4.1.0)  
FROM mono:latest  
  
# File Author / Maintainer  
MAINTAINER Yoann MALLEMANCHE (Yoannm)  
  
# Env ASF build  
ENV ASF_PATH=/asf  
ENV GIT_URL=https://github.com/JustArchi/ArchiSteamFarm.git  
ENV GIT_TAG=latest  
  
# Install dependancies  
RUN apt-get update \  
&& apt-get install -y git \  
&& rm -rf /var/lib/apt/lists/*  
  
# clone ASF  
RUN git clone ${GIT_URL} ${ASF_PATH}  
  
WORKDIR ${ASF_PATH}  
  
RUN ./cc.sh && rm out/config/example.json && rm out/config/minimal.json  
  
COPY bot.json out/config/  
  
CMD ["mono","out/ASF.exe"]  
  

