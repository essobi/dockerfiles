FROM openjdk:9-jre-slim  
MAINTAINER ElderByte <info@elderbyte.com>  
  
ENV FFMPEG_VERSION=3.4  
WORKDIR /tmp/ffmpeg  
  
# Install ffmpeg  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ffmpeg \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /  

