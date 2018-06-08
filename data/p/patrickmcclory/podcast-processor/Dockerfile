# Docker image for managing audio and video files for podcasting  
#  
# Includes AWS Cli tools and updated apt-get repo with PPA for ffmpeg  
# as well as installs of SoX and ffmpeg  
#  
# Currently installs: awscli 1.7.23  
FROM patrickmcclory/pmdev-baseimage:14.10  
MAINTAINER Patrick McClory <pmcclory@gmail.com>  
  
RUN \  
sudo add-apt-repository ppa:kirillshkrogalev/ffmpeg-next && \  
sudo apt-get update -y -qq && \  
sudo apt-get install -y sox libsox-fmt-mp3 lame -qq && \  
sudo apt-get install -y ffmpeg -qq && \  
sudo mkdir -p /media  
  
COPY normalize.sh /bin/normalize  
  
COPY processaudio.sh /bin/processaudio  
  
RUN \  
sudo chmod +x /bin/normalize && \  
sudo chmod +x /bin/processaudio  
  
VOLUME /media  
  
ENV HOME /root  
  
WORKDIR /media  
  
ENV MEDIA_SOURCE="BDMV.mov"  
ENV NOISE_PROFILE_FILE="TWFC-NoiseProfile.mp3"  
ENV AUDIO_RIP_BITRATE="256"  
ENV GENERATE_PODCAST="True"  
ENV PODCAST_BITRATE="128"  
ENV MEDIA_DIR="/media"  
ENTRYPOINT ["/bin/processaudio"]  
  
CMD ["/bin/bash"]

