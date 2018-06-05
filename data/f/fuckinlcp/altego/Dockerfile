FROM rust:latest  
  
WORKDIR /usr/src/lcpae  
COPY . .  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libopus-dev \  
libsodium-dev \  
youtube-dl \  
ffmpeg  
  
RUN cargo install  
  
CMD ["lcpae"]  

